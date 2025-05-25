import pandas as pd

def save_to_vector_store(chunks, db, table_name, embedding_model):
    embeddings = embedding_model.encode(chunks).tolist()
    data = [{"chunk_id": f"chunk_{i}", "text": chunk, "vector": embeddings[i]} for i, chunk in enumerate(chunks)]

    df = pd.DataFrame(data)
    table = db.create_table(table_name, data=df, mode="overwrite")
    return table

def retrieve_chunks(query, table, embedding_model, top_k=3):
    query_embedding = embedding_model.encode([query])[0]
    results = table.search(query_embedding).limit(top_k).to_df()
    return results["text"].tolist()
