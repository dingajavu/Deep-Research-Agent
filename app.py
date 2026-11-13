import asyncio
import json
import os
from pathlib import Path

import gradio as gr
from dotenv import load_dotenv
from styles import CSS, JS, EXAMPLES, HEADER_HTML, DEMO_BANNER_HTML
from config import NUM_CLARIFIER_QUESTIONS, ResearchContext

load_dotenv(override=True)

# Demo mode which doesn't make API calls and dynamically replays a saved run
DEMO_MODE = os.getenv("DEMO_MODE", "").strip().lower() in ("1", "true", "yes")

if DEMO_MODE:
    DEMO = json.loads((Path(__file__).parent / "demo" / "demo.json").read_text(encoding="utf-8"))
    DEMO_STEP_DELAY = 1.8  # seconds between replayed status updates
else:
    from research_manager import ResearchManager


async def clarify(query: str):
    questions = (await ResearchManager().clarify(query)).questions[:NUM_CLARIFIER_QUESTIONS]
    question_texts = [q.question for q in questions]
    answer_boxes = []
    for i in range(NUM_CLARIFIER_QUESTIONS):
        if i < len(questions):
            answer_boxes.append(gr.Textbox(label=questions[i].question, info=questions[i].why_it_matters, value="", visible=True))
        else:
            answer_boxes.append(gr.Textbox(value="", visible=False))
    return [question_texts, gr.Column(visible=True), ""] + answer_boxes


def hide_clarify_panel():
    return gr.Column(visible=False)


async def run(query: str, question_texts: list[str], *answers: str):
    ctx = ResearchContext(query=query, clarifications=list(zip(question_texts, answers)))
    async for status_update in ResearchManager().run(ctx):
        yield status_update


async def run_without_clarifications(query: str):
    async for status_update in ResearchManager().run(ResearchContext(query=query)):
        yield status_update


async def demo_clarify(query: str):
    """ Show the saved clarifying questions with the saved answers, read-only """
    saved = DEMO["clarifications"][:NUM_CLARIFIER_QUESTIONS]
    await asyncio.sleep(DEMO_STEP_DELAY)
    answer_boxes = []
    for i in range(NUM_CLARIFIER_QUESTIONS):
        if i < len(saved):
            c = saved[i]
            answer_boxes.append(gr.Textbox(label=c["question"], info=c["why_it_matters"], value=c["answer"], visible=True, interactive=False))
        else:
            answer_boxes.append(gr.Textbox(value="", visible=False))
    return [[c["question"] for c in saved], gr.Column(visible=True), ""] + answer_boxes


async def demo_run(*_):
    """ Replay the saved run's status updates, then show the saved report """
    searches = DEMO.get("searches", [])
    search_list = "\n".join(f"- {s['query']}" for s in searches)
    steps = [
        "Starting research...",
        f"Searches planned, starting {len(searches)} searches...\n\n{search_list}",
        "Searches complete, writing report...",
    ]
    for step in steps:
        yield step
        await asyncio.sleep(DEMO_STEP_DELAY)
    yield DEMO["markdown_report"]


with gr.Blocks(title="Deep Research") as ui:
    gr.HTML(HEADER_HTML)
    if DEMO_MODE:
        gr.HTML(DEMO_BANNER_HTML)

    with gr.Row(elem_classes="dr-query-row"):
        query_textbox = gr.Textbox(
            value=DEMO["query"] if DEMO_MODE else "",
            interactive=not DEMO_MODE,
            placeholder="Type a research question/topic...",
            show_label=False,
            container=False,
            autofocus=not DEMO_MODE,
            elem_id="dr-query",
            scale=5,
        )
        run_button = gr.Button("Investigate", variant="primary", elem_id="dr-run", scale=1)

    if not DEMO_MODE:
        gr.HTML('<div class="dr-examples-label">Try one</div>')
        gr.Examples(examples=EXAMPLES, inputs=query_textbox, elem_id="dr-examples")

    question_state = gr.State([])

    with gr.Column(visible=False, elem_id="dr-clarify") as clarify_panel:
        gr.HTML('<div class="dr-examples-label">A few questions to focus the research</div>')
        answer_textboxes = [
            gr.Textbox(placeholder="Leave blank if you have no preference", visible=False)
            for _ in range(NUM_CLARIFIER_QUESTIONS)
        ]
        with gr.Row():
            start_button = gr.Button("Start research", variant="primary", elem_id="dr-start")
            skip_button = gr.Button("Skip", variant="secondary", elem_id="dr-skip", visible=not DEMO_MODE)

    report = gr.Markdown(elem_id="dr-report")

    clarify_function = demo_clarify if DEMO_MODE else clarify
    clarify_outputs = [question_state, clarify_panel, report] + answer_textboxes
    run_button.click(clarify_function, inputs=query_textbox, outputs=clarify_outputs)
    query_textbox.submit(clarify_function, inputs=query_textbox, outputs=clarify_outputs)

    start_button.click(hide_clarify_panel, outputs=clarify_panel).then(
        demo_run if DEMO_MODE else run, inputs=[query_textbox, question_state] + answer_textboxes, outputs=report
    )
    if not DEMO_MODE:
        skip_button.click(hide_clarify_panel, outputs=clarify_panel).then(
            run_without_clarifications, inputs=query_textbox, outputs=report
        )


if __name__ == "__main__":
    ui.launch(css=CSS, js=JS, theme=gr.themes.Base())
