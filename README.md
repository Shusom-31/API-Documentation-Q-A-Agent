
# API Documentation Q&A Agent

## 🧾 Overview

**DocAI** is an intelligent assistant that helps users query any online documentation using natural language. It combines web scraping, embedding-based vector search with LanceDB, and a powerful Groq LLM backend to deliver accurate, context-aware answers from technical content.


## 🚀Features

- ✅ Scrapes and chunks documentation content from any given URL
- ✅ Converts chunks into vector embeddings using `sentence-transformers`
- ✅ Stores and queries embeddings using **LanceDB**
- ✅ Uses **phi's Agent** with **Groq LLMs** to answer user questions
- ✅ Clean and interactive Streamlit interface
- ✅ Persistent chat history (JSON)

## 🧱 Tech Stack



| **Component**       | **Choice(s)**                        | **Why This Choice? (Overview)**                                                                        |
| ------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| **Language**        | Python                               | Widely used for AI, NLP, and web scraping. Fast to prototype and supported by rich libraries.          |
| **Framework**       | Phidata                              | Simplifies building AI agents by managing LLMs, prompts, memory, and context efficiently.              |
| **Vector DB**       | LanceDB                              | Fast, local vector search engine suited for small to mid-scale semantic applications.                  |
| **Embedding Model** | `all-MiniLM-L6-v2` from Sentence Transformers                     | Lightweight yet effective for semantic search, balancing performance and accuracy.                     |
| **Chunking Method** | LangChain RecursiveCharacterSplitter | Maintains semantic coherence while breaking long texts into token-limited chunks for better retrieval. |
| **LLM Provider**    | Groq (model: `llama-3-70b-verrsatile`)     | Offers ultra-fast, low-latency inference ideal for real-time QA on large documents.                    |
| **Interface**       | Streamlit                            | Enables quick UI development in Python, perfect for interactive ML-based applications.                 |
| **Chat History**    | JSON file-based                      | Lightweight, persistent, and human-readable format for storing chat logs without needing a database.   |



## ⚙️Libraries & Tools:
  
  *Environment & System
  - `import os `                          
  - `from dotenv import load_dotenv`       
  
  *Web Scraping
  - `import requests `                     
  - `from bs4 import BeautifulSoup `       
  
  *Embeddings & AI
  - `from sentence_transformers import SentenceTransformer`   
  - `from phi.agent import Agent `         
  - `from phi.model.groq import Groq `    
  
  *Data Handling
  - `import pandas as pd  `               
  
  *Vector Database
  - `import lancedb   `
                 
  *Text chunking
  - `from langchain.text_splitter import RecursiveCharacterTextSplitter  `
    
  *Frontend / UI
  - `import streamlit as st  `            
  
  


## 🛠️ Setup & Configuration

  
1. **Create Environment & Install Dependencies**
   ```sh
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. **Environment Variables**
      Create a `.env` file :
    ```sh
    GROQ_API_KEY=your_groq_api_key_here
   ```
  

3. **Run the Application**
   ```sh
   streamlit run main.py
   ```

## 📁 Project Structure

```
├── lance_data                  
├── .env                   
├── script/
│   ├── scraper.py          
│   ├── Chunk_docs.py       
│   ├── db_utils.py         
│   ├── agent_config.py     
│   └── Chat_history.py     
├── main.py
├── chat_history.json           
├── requirements.txt       
└── README.md

```            


## 💡 How It Works
- 1.User enters a documentation URL
- 2.The content is scraped using BeautifulSoup
- 3.Text is split into chunks and embedded with sentence-transformers
- 4.Chunks are stored and indexed in LanceDB
- 5.A user query is embedded and compared for similarity
- 6.Top relevant chunks are passed to Groq LLM via phi.Agent for an answe









