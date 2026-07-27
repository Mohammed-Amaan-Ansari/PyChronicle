from pathlib import Path

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container
from textual.widgets import Header, Footer, Static

from pychronicle.ui.loader import load_source_code
from pychronicle.ui.trace_loader import load_trace


class PyChronicleApp(App):

    CSS_PATH = "app.tcss"

    TITLE = "PyChronicle"
    SUB_TITLE = "Time Travel Debugger"

    BINDINGS = [
        Binding("n", "next_trace", "Next"),
        Binding("p", "previous_trace", "Previous"),
        Binding("q", "quit_app", "Quit"),
    ]

    def compose(self) -> ComposeResult:

        # -----------------------------
        # Load source code
        # -----------------------------
        sample = (
            Path(__file__).resolve().parents[2]
            / "examples"
            / "trace_demo.py"
        )

        code = load_source_code(sample)

        # -----------------------------
        # Load execution trace
        # -----------------------------
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

        # -----------------------------
        # UI
        # -----------------------------
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

    # --------------------------------------------------
    # Actions
    # --------------------------------------------------

    def action_next_trace(self) -> None:
        """Go to next trace."""
        self.notify("Next trace (Implemented in Week 3)")

    def action_previous_trace(self) -> None:
        """Go to previous trace."""
        self.notify("Previous trace (Implemented in Week 3)")

    def action_quit_app(self) -> None:
        """Exit application."""
        self.exit()


if __name__ == "__main__":
    PyChronicleApp().run()