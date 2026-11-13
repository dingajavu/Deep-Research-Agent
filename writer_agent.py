# Imports

from agents import Agent, Runner
from config import WRITER_INSTRUCTIONS, ReportData, MODEL_NAME, ResearchContext 

writer_agent = Agent(name="Writer Agent", instructions=WRITER_INSTRUCTIONS, model=MODEL_NAME, output_type=ReportData)


async def write_report(ctx: ResearchContext, search_results: list[str]) -> ReportData: 
    """ Write the report for the query """
    input_message = f"{ctx.to_prompt()}\nSummarized search results: {search_results}" 
    result = await Runner.run(writer_agent, input_message)
    return result.final_output
