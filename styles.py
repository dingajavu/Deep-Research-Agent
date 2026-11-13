EXAMPLES = [
    "Most popular AI Agent frameworks in 2026",
    "Most commercially successful Agentic AI implementations in 2026"
]

HEADER_HTML = """
<div class="dr-brand">
    <svg class="dr-mark" viewBox="0 0 64 64" aria-hidden="true">
        <defs><path id="dr-drop" d="M32 11 C31.335 8.9 30.1 6.4 30.1 4.8 A1.9 1.9 0 0 1 33.9 4.8 C33.9 6.4 32.665 8.9 32 11 Z" /></defs>
        <use class="dr-drop" href="#dr-drop" transform="rotate(0 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(15 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(30 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(45 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(60 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(75 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(90 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(105 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(120 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(135 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(150 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(165 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(180 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(195 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(210 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(225 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(240 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(255 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(270 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(285 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(300 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(315 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(330 32 32)" />
        <use class="dr-drop" href="#dr-drop" transform="rotate(345 32 32)" />
        <circle class="dr-dot" cx="32.00" cy="14.00" r="1.2" />
        <circle class="dr-dot" cx="36.66" cy="14.61" r="1.2" />
        <circle class="dr-dot" cx="41.00" cy="16.41" r="1.2" />
        <circle class="dr-dot" cx="47.59" cy="23.00" r="1.2" />
        <circle class="dr-dot" cx="49.39" cy="27.34" r="1.2" />
        <circle class="dr-dot" cx="50.00" cy="32.00" r="1.2" />
        <circle class="dr-dot" cx="49.39" cy="36.66" r="1.2" />
        <circle class="dr-dot" cx="47.59" cy="41.00" r="1.2" />
        <circle class="dr-dot" cx="44.73" cy="44.73" r="1.2" />
        <circle class="dr-dot" cx="41.00" cy="47.59" r="1.2" />
        <circle class="dr-dot" cx="36.66" cy="49.39" r="1.2" />
        <circle class="dr-dot" cx="32.00" cy="50.00" r="1.2" />
        <circle class="dr-dot" cx="27.34" cy="49.39" r="1.2" />
        <circle class="dr-dot" cx="23.00" cy="47.59" r="1.2" />
        <circle class="dr-dot" cx="19.27" cy="44.73" r="1.2" />
        <circle class="dr-dot" cx="16.41" cy="41.00" r="1.2" />
        <circle class="dr-dot" cx="14.61" cy="36.66" r="1.2" />
        <circle class="dr-dot" cx="14.00" cy="32.00" r="1.2" />
        <circle class="dr-dot" cx="14.61" cy="27.34" r="1.2" />
        <circle class="dr-dot" cx="16.41" cy="23.00" r="1.2" />
        <circle class="dr-dot" cx="19.27" cy="19.27" r="1.2" />
        <circle class="dr-dot" cx="23.00" cy="16.41" r="1.2" />
        <circle class="dr-dot" cx="27.34" cy="14.61" r="1.2" />
        <circle class="dr-core" cx="32" cy="32" r="9" />
        <circle class="dr-orbit" cx="44.73" cy="19.27" r="5" />
    </svg>
    <div class="dr-titles">
        <h1>Research Companion</h1>
        <p>Ask once. Get the full report.</p>
    </div>
</div>
"""

CSS = """
@import url("https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap");

.gradio-container {
    /* Palette: "Quiet Slate". amber = primary accent (teal), blue = headings/links, purple = hover/secondary */
    --dr-bg: #f4f6f8;
    --dr-surface: #ffffff;
    --dr-line: #1c2733;
    --dr-line-soft: #dbe1e7;
    --dr-text: #1c2733;
    --dr-muted: #64748b;
    --dr-amber: #0d9488;
    --dr-blue: #0f766e;
    --dr-purple: #334155;
    --dr-on-accent: #ffffff;
    --dr-font: "IBM Plex Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
    --dr-mono: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;

    max-width: 1080px !important;
    margin: 0 auto !important;
    padding: 2.5rem 2rem 4rem !important;
    background: var(--dr-bg) !important;
    color: var(--dr-text) !important;
    font-family: var(--dr-font) !important;
}

.gradio-container.dark,
.dark .gradio-container,
body.dark .gradio-container,
html.dark .gradio-container {
    --dr-bg: #0f151b;
    --dr-surface: #18212a;
    --dr-line: #e2e8f0;
    --dr-line-soft: #2a3744;
    --dr-text: #e2e8f0;
    --dr-muted: #8294a6;
    --dr-amber: #2dd4bf;
    --dr-blue: #5eead4;
    --dr-purple: #cbd5e1;
    --dr-on-accent: #0f151b;
}

body { background: var(--dr-bg, #f4f6f8); }

/* === HEADER === */
.dr-brand {
    display: grid;
    grid-template-columns: auto 1fr;
    align-items: center;
    gap: 1.4rem;
    padding-bottom: 1.25rem;
    border-bottom: 3px solid var(--dr-line);
    margin-bottom: 2.5rem;
}

/* Round logo: ring of inward-pointing teardrops, ring of dots, core and companion dot */
.dr-mark { width: 56px; height: 56px; display: block; overflow: visible; }
.dr-drop  { fill: var(--dr-line); }
.dr-dot   { fill: var(--dr-blue); }
.dr-core  { fill: var(--dr-amber); }
.dr-orbit      { fill: var(--dr-purple); stroke: var(--dr-bg); stroke-width: 2.5; }

.dr-titles h1 {
    font-size: clamp(1.8rem, 4vw, 2.8rem);
    font-weight: 700;
    letter-spacing: -0.03em;
    margin: 0;
    line-height: 1;
    text-transform: uppercase;
    color: var(--dr-text);
}

.dr-titles p {
    font-family: var(--dr-mono);
    font-size: 0.7rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin: 0.55rem 0 0;
    color: var(--dr-muted);
}

/* === QUERY ROW === */
.dr-query-row {
    gap: 0 !important;
    align-items: stretch !important;
}

#dr-query, #dr-query > div, #dr-query .wrap, #dr-query .form, #dr-query .block {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    border-radius: 0 !important;
}

#dr-query textarea, #dr-query input {
    background: var(--dr-surface) !important;
    color: var(--dr-text) !important;
    border: 2px solid var(--dr-line) !important;
    border-radius: 0 !important;
    padding: 1.05rem 1.2rem !important;
    font-size: 1.05rem !important;
    font-family: inherit !important;
    box-shadow: none !important;
    line-height: 1.45 !important;
    resize: none !important;
    min-height: 56px !important;
    transition: border-color 0.15s, box-shadow 0.15s !important;
}

#dr-query textarea:focus, #dr-query input:focus {
    outline: none !important;
    border-color: var(--dr-blue) !important;
    box-shadow: 6px 6px 0 0 var(--dr-blue) !important;
}

#dr-query textarea::placeholder, #dr-query input::placeholder {
    color: var(--dr-muted) !important;
    opacity: 1 !important;
}

#dr-run {
    background: var(--dr-amber) !important;
    color: var(--dr-on-accent) !important;
    border: 2px solid var(--dr-line) !important;
    border-left: none !important;
    border-radius: 0 !important;
    font-weight: 800 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.14em !important;
    font-size: 0.85rem !important;
    box-shadow: none !important;
    transition: background 0.15s, color 0.15s, transform 0.08s !important;
    min-width: 150px !important;
    padding: 1rem 1.5rem !important;
}

#dr-run:hover {
    background: var(--dr-purple) !important;
    color: var(--dr-on-accent) !important;
}

#dr-run:active { transform: translate(2px, 2px) !important; }

/* === EXAMPLES === */
.dr-examples-label {
    font-family: var(--dr-mono);
    font-size: 0.65rem;
    letter-spacing: 0.28em;
    color: var(--dr-muted);
    text-transform: uppercase;
    margin: 2rem 0 0.85rem 0;
    display: flex;
    align-items: center;
    gap: 0.85rem;
}

.dr-examples-label::after {
    content: "";
    flex: 1;
    height: 1px;
    background: var(--dr-line-soft);
}

#dr-examples, #dr-examples > div, #dr-examples .wrap, #dr-examples .block {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    box-shadow: none !important;
}

#dr-examples label, #dr-examples .label-wrap, #dr-examples > div > .label-wrap {
    display: none !important;
}

#dr-examples table {
    border-collapse: separate !important;
    border-spacing: 0 !important;
    width: auto !important;
    background: transparent !important;
    border: none !important;
}

#dr-examples thead { display: none !important; }

#dr-examples tbody { background: transparent !important; }

#dr-examples tr {
    background: transparent !important;
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 8px !important;
    border: none !important;
}

#dr-examples td, #dr-examples button {
    background: var(--dr-surface) !important;
    border: 1.5px solid var(--dr-line-soft) !important;
    padding: 0.7rem 1.05rem !important;
    cursor: pointer !important;
    transition: border-color 0.15s, color 0.15s, transform 0.1s !important;
    font-size: 0.9rem !important;
    color: var(--dr-text) !important;
    border-radius: 0 !important;
    margin: 0 !important;
    text-align: left !important;
    box-shadow: none !important;
}

#dr-examples td:hover, #dr-examples button:hover {
    border-color: var(--dr-purple) !important;
    color: var(--dr-purple) !important;
    transform: translateY(-1px);
}

/* === REPORT === */
#dr-report {
    margin-top: 2.5rem !important;
    padding: 0 !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--dr-text) !important;
    min-height: 40px;
}

#dr-report > div, #dr-report .prose {
    background: transparent !important;
    color: var(--dr-text) !important;
}

#dr-report:not(:empty) {
    border-top: 1px solid var(--dr-line-soft) !important;
    padding-top: 1.75rem !important;
}

#dr-report h1 {
    font-size: 1.85rem;
    font-weight: 900;
    color: var(--dr-blue);
    border-bottom: 2px solid var(--dr-line);
    padding-bottom: 0.45rem;
    margin: 1.5rem 0 1rem;
    letter-spacing: -0.025em;
}

#dr-report h2 {
    font-size: 1.35rem;
    color: var(--dr-purple);
    font-weight: 800;
    margin-top: 1.75rem;
    letter-spacing: -0.015em;
}

#dr-report h3 {
    font-size: 1.1rem;
    color: var(--dr-text);
    font-weight: 800;
    margin-top: 1.5rem;
}

#dr-report :is(p, li, td, blockquote, pre, code, em, strong) { color: var(--dr-text) !important; }
#dr-report code, #dr-report pre { font-family: var(--dr-mono) !important; }

#dr-report p { line-height: 1.7; }

#dr-report a {
    color: var(--dr-blue);
    text-decoration: underline;
    text-decoration-thickness: 2px;
    text-underline-offset: 3px;
}

#dr-report a:hover { color: var(--dr-amber); }

#dr-report code {
    background: var(--dr-surface);
    border: 1px solid var(--dr-line-soft);
    padding: 0.1rem 0.4rem;
    font-size: 0.92em;
    border-radius: 0;
}

#dr-report pre {
    background: var(--dr-surface);
    border: 1.5px solid var(--dr-line-soft);
    border-radius: 0;
    padding: 1rem 1.25rem;
}

#dr-report blockquote {
    border-left: none !important;
    background: var(--dr-surface);
    padding: 1rem 1.25rem;
    margin: 1rem 0;
    color: var(--dr-text);
}

#dr-report ul, #dr-report ol { padding-left: 1.5rem; }
#dr-report li { margin: 0.3rem 0; line-height: 1.6; }

#dr-report table {
    border-collapse: collapse;
    border: 1.5px solid var(--dr-line);
}

#dr-report th, #dr-report td {
    border: 1px solid var(--dr-line-soft);
    padding: 0.5rem 0.85rem;
    text-align: left;
}

#dr-report th {
    background: var(--dr-surface);
    font-weight: 800;
    color: var(--dr-blue);
}

footer { display: none !important; }

@media (max-width: 700px) {
    .gradio-container { padding: 1.5rem 1rem 3rem !important; }
    .dr-query-row { flex-direction: column !important; }
    #dr-run {
        border-left: 2px solid var(--dr-line) !important;
        border-top: none !important;
        width: 100% !important;
    }
}
"""

JS = """
() => {
    const focus = () => {
        const el = document.querySelector("#dr-query textarea, #dr-query input");
        if (el) { el.focus(); return true; }
        return false;
    };
    if (!focus()) {
        let tries = 0;
        const i = setInterval(() => {
            if (focus() || ++tries > 20) clearInterval(i);
        }, 100);
    }
}
"""
