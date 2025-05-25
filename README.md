
# API Documentation Q&A Agent

## Overview

**DocBot** is an intelligent assistant that helps users query any online documentation using natural language. It combines web scraping, embedding-based vector search with LanceDB, and a powerful Groq LLM backend to deliver accurate, context-aware answers from technical content.


## Features

- ✅ Scrapes and chunks documentation content from any given URL
- ✅ Converts chunks into vector embeddings using `sentence-transformers`
- ✅ Stores and queries embeddings using **LanceDB**
- ✅ Uses **phi's Agent** with **Groq LLMs** to answer user questions
- ✅ Clean and interactive Streamlit interface

## Technologies Used
- **Programming Language**: Python
- **Framework**: Streamlit
- **AI Model**: Groq (Llama 3.3-70b-versatile)
- **Libraries & Tools**:
  - `phi.agent` (AI agent management)
  - `phi.model.groq` (AI model integration)
  - `phi.tools.email` (Email generation and sending)
  - `phi.tools.googlesearch` (Web search integration)
  - `phi.tools.website` (Extracting website information)
  - `PyMuPDF (fitz)` (PDF text extraction)
  - `json` (Conversation history management)
  - `dotenv` (Environment variable management)
 
  # Environment & System
  -`import os `                           # Access environment and file system
  -`from dotenv import load_dotenv`       # Load environment variables (e.g. API keys)

  #  Web Scraping
  -`import requests `                     # Fetch content from documentation URLs
  -`from bs4 import BeautifulSoup `       ## Parse HTML content

  #  Embeddings & AI
  -`from sentence_transformers import SentenceTransformer`   # Create vector embeddings for text
  -`from phi.agent import Agent `         # Used to define the intelligent agent's behavior and role
  -`from phi.model.groq import Groq `     # Connects the agent with Groq’s powerful LLM backend

  #  Data Handling
  =`import pandas as pd  `                # For organizing and structuring data before inserting into LanceDB

  #  Vector Database
  -`import lancedb   `                    # High-performance vector database

  #  Frontend / UI
  -`import streamlit as st  `             # To create an interactive and user-friendly web interface


## Setup & Configuration
1. **Environment Variables**
   Create a .env file in the root directory:
    ```sh
    GROQ_API_KEY=your_groq_api_key_here
   ```
  

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```sh
   streamlit run main.py
   ```


## How It Works
1.User enters a documentation URL
2.The content is scraped using BeautifulSoup
3.Text is split into chunks and embedded with sentence-transformers
4.Chunks are stored and indexed in LanceDB
5.A user query is embedded and compared for similarity
6.Top relevant chunks are passed to Groq LLM via phi.Agent for an answe

Use Cases
-Ask questions about open-source libraries or web APIs
-Quickly find relevant documentation pieces
-Build personal AI research assistants








