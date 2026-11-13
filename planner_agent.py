# Imports

from agents import Agent, Runner
import asyncio
from config import MODEL_NAME, WebSearchPlan, PLANNER_INSTRUCTIONS, ResearchContext  
from search_agent import search

planner_agent = Agent(name="Planner Agent", instructions=PLANNER_INSTRUCTIONS, model=MODEL_NAME, output_type=WebSearchPlan)

async def plan_searches(ctx: ResearchContext) -> WebSearchPlan: 
    """ Plan the searches to perform for the query """
    result = await Runner.run(planner_agent, ctx.to_prompt())  
    return result.final_output

async def perform_searches(search_plan: WebSearchPlan) -> list[str]:
    """ Perform the searches to perform for the query """
    tasks = [search(item) for item in search_plan.searches]
    return await asyncio.gather(*tasks)
