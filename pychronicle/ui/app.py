from pathlib import Path

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Static

from pychronicle.ui.loader import load_source_code
from pychronicle.ui.trace_loader import load_trace


class PyChronicleApp(App):

    CSS_PATH = "app.tcss"

    TITLE = "PyChronicle"
    SUB_TITLE = "Time Travel Debugger"

    BINDINGS = [
        ("n", "next_trace", "Next"),
        ("p", "previous_trace", "Previous"),
    ]

    def compose(self) -> ComposeResult:

        # Load source code
        sample = (
            Path(__file__).resolve().parents[2]
            / "examples"
            / "trace_demo.py"
        )

        code = load_source_code(sample)

        # Load execution trace
        trace = load_trace()

        current = trace[0] if trace else None

        if current:
            details = f"""
Execution Details

Event      : {current[1]}

Function   : {current[3]}

Line       : {current[2]}

Variables

{current[4]}
"""
        else:
            details = """
Execution Details

No execution trace found.
"""

        yield Header()

        with Container(id="body"):

            yield Static(
                code,
                id="code_view",
            )

            yield Static(
                details,
                id="details",
            )

        yield Static(
            "🕒 Timeline (Coming Soon)",
            id="timeline",
        )

        yield Footer()

    def action_next_trace(self):
        self.notify("Next trace (Coming in Week 3)")

    def action_previous_trace(self):
        self.notify("Previous trace (Coming in Week 3)")


if __name__ == "__main__":
    PyChronicleApp().run()