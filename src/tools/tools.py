import os

import requests
from dotenv import load_dotenv
from langchain.tools import tool
from rich import print
from tavily import TavilyClient

load_dotenv()

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def web_search(query: str):
    """Search the web for reliable and latest information on a topic.
    Returns Title, URLs and, Content"""

    results = tavily_client.search(query=query, max_results=2)

    print(results)
