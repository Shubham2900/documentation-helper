import asyncio
import os
import ssl
from typing import Any, Dict, List

import certifi
from PIL.ImageChops import overlay
from dotenv import load_dotenv
from gitdb.fun import chunk_size
from langchain_chroma import Chroma
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_tavily import TavilyCrawl, TavilyExtract, TavilyMap, tavily_extract

from logger import (Colors, log_error, log_header, log_info, log_success,
                    log_warning)

load_dotenv()
# Configure SSL context to use certifi certificates
ssl_context = ssl.create_default_context(cafile=certifi.where())
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

embeddings = OllamaEmbeddings(
    model="snowflake-arctic-embed2:latest"
)

vectorstore = PineconeVectorStore(index_name=os.environ["INDEX_NAME"], embedding=embeddings)
tavily_extract = TavilyExtract()
tavily_map = TavilyMap(max_depth=5, max_breadth=20, max_pages=20)
tavily_crawl = TavilyCrawl()



async def main():
    """Main async function to orchestrate the entire process"""

if __name__ == "__main__":
    main()