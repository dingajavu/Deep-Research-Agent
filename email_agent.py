# Imports
from agents import Agent, Runner, function_tool
from agents.model_settings import ModelSettings
from config import EMAIL_INSTRUCTIONS, ReportData, MODEL_NAME
from messenger import send_email

settings = ModelSettings(tool_choice="required")

@function_tool
def send_email_tool(subject: str, text_body: str, html_body: str) -> str:
    """
    Send out an email with the given subject and the research report
    
    Args:
        subject: The subject of the email
        text_body: The body of the email as plain text
        html_body: The HTML body of the email
    """
    send_email(subject, text_body, html_body)
    return "Email sent successfully"


email_agent = Agent(
    name="Email Agent", 
    instructions=EMAIL_INSTRUCTIONS, 
    tools=[send_email_tool], 
    model=MODEL_NAME, 
    model_settings=settings
    )


async def send_report_email(report: ReportData) -> None: 
    await Runner.run(email_agent, report.markdown_report)  
