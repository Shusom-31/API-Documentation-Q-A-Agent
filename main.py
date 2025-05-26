import os
import streamlit as st
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import lancedb

from script.scraper import scrape_url
from script.Chunk_docs import chunk_text
from script.db_utils import save_to_vector_store, retrieve_chunks
from script.agent_config import agent
from script.Chat_history import save_chat_entry, load_chat_history  # Add load if you want to show history

# === Load API Key ===
load_dotenv()
embedding_model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")
db_dir = "lance_data"
table_name = "url_chunks"

if not os.path.exists(db_dir):
    os.makedirs(db_dir)

db = lancedb.connect(db_dir)

# === Streamlit UI ===
def main():

    st.set_page_config(page_title="URL Doc Assistant")
    st.title("🌐 DocAI – Ask Questions from a Documentation URL")

    url = st.text_input("Enter documentation URL")
    
    if  st.button("Load & Process"):
        with st.spinner("Scraping and indexing..."):
            text = scrape_url(url)
            if text:
                chunks = chunk_text(text)
                table = save_to_vector_store(chunks, db, table_name, embedding_model)
                st.success(f"{len(chunks)} chunks saved to VectorDB!")

    if table_name in db.table_names():
        query = st.chat_input("Ask your question...")
        if query:
            with st.spinner("Searching and responding..."):
                table = db.open_table(table_name)
                relevant_chunks = retrieve_chunks(query, table, embedding_model)
                context = "\n".join(relevant_chunks)

                prompt = (
                    f"Documentation Context:\n{context}\n\n"
                    f"User Question:\n{query}\n\n"
                    f"Answer based only on the above."
                )
                response = agent.run(prompt)

                # Save chat history
                save_chat_entry(query, response.content)

                st.chat_message("assistant").markdown(response.content)

if __name__ == "__main__":
    main()
