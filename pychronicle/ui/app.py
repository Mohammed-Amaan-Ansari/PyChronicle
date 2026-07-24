from pathlib import Path

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Static

from pychronicle.ui.loader import load_source_code


class PyChronicleApp(App):

    CSS_PATH = "app.tcss"

    TITLE = "PyChronicle"
    SUB_TITLE = "Time Travel Debugger"

    def compose(self) -> ComposeResult:

        # Load the source code
        sample = (
            Path(__file__).resolve().parents[2]
            / "examples"
            / "trace_demo.py"
        )

        code = load_source_code(sample)

        yield Header()

        with Container(id="body"):

            yield Static(
                code,
                id="code_view",
            )

            yield Static(
                """Execution Details

Event:
Function:
Line:
Variables:
""",
                id="details",
            )

        yield Static(
            "🕒 Timeline (Coming Soon)",
            id="timeline",
        )

        yield Footer()


if __name__ == "__main__":
    PyChronicleApp().run()