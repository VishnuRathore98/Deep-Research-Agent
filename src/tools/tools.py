import requests
import re
import json
from langchain.tools import tool
from rich import print
from tavily import TavilyClient
import trafilatura
from src.config import settings

tavily_client = TavilyClient(api_key=settings.TAVILY_API_KEY)


# @tool
def web_search(query: str):
    """Search the web for reliable and latest information on a topic.
    Returns Title, URLs and, Content"""

    results = tavily_client.search(query=query, max_results=2)

    print(results)


def scrape_url(url: str):
    """
    scrape and extract data from url and clean it to make it readable content.
    """

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            "AppleWebKit/537.36 (KHTML, like Gecko)"
            "Chrome/124.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/",
    }

    response = requests.get(
        url=url,
        headers=headers,
    )

    html = response.text

    extracted = trafilatura.extract(
        html,
        include_tables=False,
    )

    if extracted and (len(extracted.strip()) > 200):
        cleaned = re.sub(r"\s+", " ", extracted)
        return cleaned[:5000]

    # print(json.loads(response.text))
    return "Could not get data"
