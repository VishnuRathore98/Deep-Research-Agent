from rich import print

from src.agents.agents import (
    build_critique_agent,
    build_reader_agent,
    build_search_agent,
    build_writer_agent,
)


def run_research_pipeline(topic: str):

    state = {}

    search_agent = build_search_agent()
    print("\nSuccessfully created search tool.")
    search_result = search_agent.invoke(
        {
            "messages": [
                (
                    "user",
                    f"Find recent, reliable and detailed information about: {topic}",
                ),
            ]
        }
    )
    print("\nGot search result.\n")
    state["search_results"] = search_result["messages"][-1].content
    print("Search Results: \n", state["search_results"])

    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke(
        {
            "messages": (
                [
                    "user",
                    f"Based on the following search results about '{topic}', "  # noqa: ISC004
                    f"pick the most relevant URL and scrape it for deeper content.\n\n"
                    f"Search Results:\n{state['search_results'][:2000]}",
                ]
            )
        }
    )
    state["scraped_content"] = reader_result["messages"][-1].content
    print("\n\nScraped Content: \n", state["scraped_content"])

    research_combined = (
        f"SEARCH RESULTS: \n {state['search_results']}\n\n"
        f"DETAILED SCRAPED CONTENT: \n {state['scraped_content']}"
    )

    writer_agent = build_writer_agent()
    state["report"] = writer_agent.invoke(
        {
            "topic": topic,
            "research": research_combined,
        }
    )
    print("\n\nReport Generated: \n", state["report"])

    critique_agent = build_critique_agent()
    state["feedback"] = critique_agent.invoke(
        {
            "report": state["report"],
        }
    )
    print("\n\nFeedback: \n", state["feedback"])

    print("\n\nFinal Result: \n", state)
