# Imports
from agents import Agent, WebSearchTool, Runner
from agents.model_settings import ModelSettings
from config import MODEL_NAME, WebSearchItem, SEARCH_INSTRUCTIONS


settings = ModelSettings(tool_choice="required")
tools = [WebSearchTool()]                              # Tool instance created

# Agent definition

search_agent = Agent(name="Search Agent", instructions=SEARCH_INSTRUCTIONS, tools=tools, model=MODEL_NAME, model_settings=settings)

async def search(item: WebSearchItem) -> str | None:
    """ Perform a search for the query """
    input_message = f"Search term: {item.query}\nReason for searching: {item.reason}"
    result = await Runner.run(search_agent, input_message)
    return result.final_output