from pathlib import Path

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container
from textual.widgets import Header, Footer, Static

from pychronicle.ui.trace_loader import load_trace


class PyChronicleApp(App):

    CSS_PATH = "app.tcss"

    TITLE = "PyChronicle"
    SUB_TITLE = "Time Travel Debugger"

    BINDINGS = [
        Binding("n", "next_trace", "Next"),
        Binding("p", "previous_trace", "Previous"),
        Binding("home", "first_trace", "First"),
        Binding("end", "last_trace", "Last"),
        Binding("f", "jump_forward", "+5"),
        Binding("b", "jump_backward", "-5"),
        Binding("q", "quit_app", "Quit"),
    ]

    def __init__(self):
        super().__init__()

        self.sample = (
            Path(__file__).resolve().parents[2]
            / "examples"
            / "trace_demo.py"
        )

        self.trace_data = load_trace()
        self.current_index = 0
