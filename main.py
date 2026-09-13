from src.pipelines.pipeline import run_research_pipeline
from src.tools.tools import scrape_url, web_search
from src.agents.agents import llm


# web_search(query="today's whether in jodhpur, rajasthan.")

# scrape_url(
#     url="https://indianexpress.com/section/weather/jodhpur-weather-forecast-today"
# )

topic = "Current state of jobs in mobile development after AI."
run_research_pipeline(topic=topic)

# model = ChatOpenRouter(
#     model="anthropic/claude-sonnet-4.6",
#     temperature=0,
#     api_key=settings.OPEN_ROUTER_API_KEY,
#     max_tokens=1024,
# )
