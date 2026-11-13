from agents import trace, gen_trace_id
from planner_agent import plan_searches, perform_searches
from writer_agent import write_report
from email_agent import send_report_email
from clarifier_agent import get_clarifying_questions
from config import ClarifyingQuestions, ResearchContext
class ResearchManager:

    async def clarify(self, query: str) -> ClarifyingQuestions: 
        """ Phase 1: get the clarifying questions to ask the user """ 
        with trace("Clarifier trace"): 
            return await get_clarifying_questions(query) 

    async def run(self, ctx: ResearchContext): 
        """ Run the deep research process, yielding the status updates and the final report"""
        trace_id = gen_trace_id()
        with trace("Research trace", trace_id=trace_id):
            yield f"Starting research. Trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"
            search_plan = await plan_searches(ctx)
            yield f"Searches planned, starting {len(search_plan.searches)} searches..."
            search_results = await perform_searches(search_plan)
            yield "Searches complete, writing report..."
            report = await write_report(ctx, search_results)
            yield "Report written, sending email..."
            await send_report_email(report)
            yield "Email sent, research complete"
            yield report.markdown_report
