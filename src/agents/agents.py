from langchain.agents import create_agent
from langchain_core.output_parsers import StrOutputParser
from langchain_openrouter import ChatOpenRouter

from src.config import settings
from src.prompts.prompts import critique_prompt, writer_prompt
from src.tools.tools import scrape_url, web_search

llm = ChatOpenRouter(
    model=settings.OPEN_ROUTER_MODEL,
    temperature=0,
    api_key=settings.OPEN_ROUTER_API_KEY,
    max_tokens=1024,
)


def build_search_agent():

    print("\nCreating search tool...\n")

    return create_agent(
        model=llm,
        tools=[web_search],
    )


def build_reader_agent():

    print("\nCreating scrape tool...\n")
    return create_agent(
        model=llm,
        tools=[scrape_url],
    )


def build_writer_agent():

    print("\nCreating writer...\n")
    return writer_prompt | llm | StrOutputParser()


def build_critique_agent():

    print("\nCreating critique tool...\n")
    return critique_prompt | llm | StrOutputParser()
