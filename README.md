# Deep Research Agent

**[Live demo](https://huggingface.co/spaces/dingajavu/deep-research-system)**: a replay of one recorded research run.

A multi-agent deep research system built with the [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) and [Gradio](https://www.gradio.app/). Give it a topic answer and a team of agents with specualised functions scope the question with you, plans and runs the web searches in parallel, writes a detailed markdown report and emails the report to you.

## How it works

| Agent | Role |
|---|---|
| **Clarifier** | Asks a few clarifying questions to focus the search |
| **Planner** | Turns the query and your answers into a set of web searches |
| **Search** | Runs each search and summarises the results |
| **Writer** | Writes a long-form report tailored to your answers |
| **Email** | Sends the report to you as an HTML email |

You can skip the clarifying questions to research the query.

## Setup

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your-openai-key
EMAIL_ADDRESS=you@example.com
EMAIL_SMTP_SERVER=smtp.example.com
EMAIL_APP_PASSWORD=your-email-app-password
```

The report is sent from and to `EMAIL_ADDRESS` over SMTP.

## Run

```bash
uv run app.py
```

Then open the local URL Gradio prints.

## Configuration

Edit `config.py` to change the models (`MODEL_NAME` for most agents, `WRITER_MODEL` for the report writer), the number of searches (`HOW_MANY_SEARCHES`), the number of clarifying questions (`NUM_CLARIFIER_QUESTIONS`), or any agent's instructions.

## License

[MIT](LICENSE)
