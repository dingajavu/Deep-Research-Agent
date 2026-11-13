# Imports

from agents import Agent, Runner  
from config import MODEL_NAME, CLARIFIER_INSTRUCTIONS, ClarifyingQuestions  

clarifier_agent = Agent(name="Clarifier Agent", instructions=CLARIFIER_INSTRUCTIONS, model=MODEL_NAME, output_type=ClarifyingQuestions) 


async def get_clarifying_questions(query: str) -> ClarifyingQuestions:
    """ Ask clarifying questions about the research query """  
    result = await Runner.run(clarifier_agent, f"Query: {query}")  
    return result.final_output  
