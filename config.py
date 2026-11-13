from pydantic import BaseModel, Field

MODEL_NAME = "gpt-6-luna"
HOW_MANY_SEARCHES = 5
NUM_CLARIFIER_QUESTIONS = 3  

RESEARCH_TASK = "The best sports data analytics practices in 2026"


CLARIFIER_INSTRUCTIONS = f"""
You are a research scoper. Given a research query, identify the ambiguities that would
most change how the research is done: scope, time frame, audience, depth, region, angle,
or what to exclude. Ask exactly {NUM_CLARIFIER_QUESTIONS} short, specific questions. Do not
ask about things already clear and apparent from the query.
"""

SEARCH_INSTRUCTIONS = """
You are a research assistant. Given a search term, you search the web for that term and
produce a concise summary of the results. The summary must 2-3 paragraphs and less than 300 words.
Capture the main points and be succinct. Reply only with the summary.
"""

PLANNER_INSTRUCTIONS = f"""
You are a research assistant. Given a user query, come up with a set of web searches
to perform to best answer the query. Output {HOW_MANY_SEARCHES} terms to query for.
If the user has provided clarifications, treat them as requirements: the searches and
their reasons must reflect the scope, time frame, audience, focus and exclusions they specify.
"""

WRITER_INSTRUCTIONS = """
You are a senior researcher tasked with writing a cohesive report for a research query.
You will be provided with the original query, and some research.
Generate a comprehensive report based on the research and the query.
The final output should be in markdown format, and it should be lengthy and detailed. Aim
for 5-10 pages of content, at least 1000 words.
If the user has provided clarifications, tailor the report to them: match the requested
audience, depth, scope and emphasis, and leave out anything they asked to exclude.
"""

EMAIL_INSTRUCTIONS = """
You are provided with a detailed report. Use your tool to send an email, converting the report into
a clean, well presented HTML email with an appropriate subject line.
"""

class ClarifyingQuestion(BaseModel):
    question: str = Field(description="The question to ask the user.")
    why_it_matters: str = Field(description="How the answer will change the research direction.")

class ClarifyingQuestions(BaseModel): 
    questions: list[ClarifyingQuestion] = Field(description="The clarifying questions to ask the user.") 


class ResearchContext(BaseModel): 
    query: str 
    clarifications: list[tuple[str, str]] = [] 

    def to_prompt(self) -> str:  
        lines = [f"Original query: {self.query}"] 
        answered = [(q, a) for q, a in self.clarifications if a.strip()] 
        if answered:  
            lines.append("User clarifications (treat these as requirements):")
            lines += [f"- Q: {q}\n  A: {a}" for q, a in answered] 
        return "\n".join(lines) 


class WebSearchItem(BaseModel):
    reason: str = Field(description="Your reasoning for why this search is important to the query.")
    query: str = Field(description="The search term to use for the web search.")


class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="A list of web searches to perform to best answer the query.")


class ReportData(BaseModel):
    short_summary: str = Field(description="A short 2-3 sentence summary of the findings.")
    markdown_report: str = Field(description="The final report")
    follow_up_questions: list[str] = Field(description="Suggested topics to research further")
