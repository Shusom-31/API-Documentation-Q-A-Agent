
import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import lancedb
import pandas as pd
import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq

# === Load API Key ===
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# === Embedding Model + LanceDB Setup ===
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
db_dir = "lance_data"
table_name = "url_chunks"

if not os.path.exists(db_dir):
    os.makedirs(db_dir)

db = lancedb.connect(db_dir)

# === Scrape Text from URL ===
def scrape_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all(["p", "li", "code"])
        text = "\n".join(p.get_text(strip=True) for p in paragraphs)
        return text
    except Exception as e:
        st.error(f"Failed to scrape URL: {e}")
        return ""

# === Chunk Text ===
def chunk_text(text, chunk_size=300):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# === Save to LanceDB Vector Store ===
def save_to_vector_store(chunks):
    embeddings = embedding_model.encode(chunks).tolist()
    data = [{"chunk_id": f"chunk_{i}", "text": chunk, "vector": embeddings[i]} for i, chunk in enumerate(chunks)]

    df = pd.DataFrame(data)
    table = db.create_table(table_name, data=df, mode="overwrite")
    return table

# === Retrieve Similar Chunks ===
def retrieve_chunks(query, table, top_k=3):
    query_embedding = embedding_model.encode([query])[0]
    results = table.search(query_embedding).limit(top_k).to_df()
    return results["text"].tolist()

# === Agent ===
agent = Agent(
    name="DocBot",
    role="Expert documentation assistant",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "Be helpful and extract info from documentation.",
        "Use only context provided to answer queries."
    ],
    markdown=True
)

# === Streamlit UI ===
def main():
    st.set_page_config(page_title="URL Doc Assistant")
    st.title("🌐 DocBot – Ask Questions from a Documentation URL")

    url = st.text_input("Enter documentation URL")

    if url and st.button("Load & Process"):
        with st.spinner("Scraping and indexing..."):
            text = scrape_url(url)
            if text:
                chunks = chunk_text(text)
                table = save_to_vector_store(chunks)
                st.success(f"{len(chunks)} chunks saved!")

    if table_name in db.table_names():
        query = st.chat_input("Ask your question...")
        if query:
            with st.spinner("Searching and responding..."):
                table = db.open_table(table_name)
                relevant_chunks = retrieve_chunks(query, table)
                context = "\n".join(relevant_chunks)

                prompt = (
                    f"Documentation Context:\n{context}\n\n"
                    f"User Question:\n{query}\n\n"
                    f"Answer based only on the above."
                )
                response = agent.run(prompt)
                st.chat_message("assistant").markdown(response.content)

if __name__ == "__main__":
    main()
