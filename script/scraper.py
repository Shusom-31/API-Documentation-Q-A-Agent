import requests
from bs4 import BeautifulSoup
import streamlit as st

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
