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

    # --------------------------------------------------
    # Helpers
    # --------------------------------------------------

    def get_current_trace(self):

        if not self.trace_data:
            return None

        return self.trace_data[self.current_index]

    def build_timeline(self) -> str:

        if not self.trace_data:
            return "🕒 No trace data available"

        total = len(self.trace_data)
        current = self.current_index + 1

        bar_length = 30

        position = int((current / total) * bar_length)

        timeline = []

        for i in range(bar_length):

            if i == position - 1:
                timeline.append("●")
            else:
                timeline.append("─")

        percentage = int((current / total) * 100)

        return (
            f"🕒 Timeline: {current}/{total}  ({percentage}%)\n"
            f"[{''.join(timeline)}]\n"
            f"Controls: N/P | Home/End | F/B | Q"
        )

    def build_code_view(self, current_line: int | None) -> str:

        with open(self.sample, "r", encoding="utf-8") as file:
            lines = file.readlines()

        output = []

        for number, line in enumerate(lines, start=1):

            prefix = "▶" if number == current_line else " "

            output.append(
                f"{prefix} {number:>3} │ {line.rstrip()}"
            )

        return "\n".join(output)

    def build_details(self) -> str:

        current = self.get_current_trace()

        if not current:
            return "No execution trace found."

        return f"""
Execution Details

Trace Index : {self.current_index + 1} / {len(self.trace_data)}

Event       : {current[1]}
Function    : {current[3]}
Line        : {current[2]}

Variables

{current[4]}
"""

    def refresh_ui(self) -> None:

        current = self.get_current_trace()

        line_number = current[2] if current else None

        self.query_one("#code_view", Static).update(
            self.build_code_view(line_number)
        )

        self.query_one("#details", Static).update(
            self.build_details()
        )

        self.query_one("#timeline", Static).update(
            self.build_timeline()
        )

    # --------------------------------------------------
    # UI
    # --------------------------------------------------

    def compose(self) -> ComposeResult:

        current = self.get_current_trace()
        line_number = current[2] if current else None

        yield Header()

        with Container(id="body"):

            yield Static(
                self.build_code_view(line_number),
                id="code_view",
            )

            yield Static(
                self.build_details(),
                id="details",
            )

        yield Static(
            self.build_timeline(),
            id="timeline",
        )

        yield Footer()

    # --------------------------------------------------
    # Navigation Actions
    # --------------------------------------------------

    def action_next_trace(self):
        if self.current_index < len(self.trace_data) - 1:
            self.current_index += 1
            self.refresh_ui()

    def action_previous_trace(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.refresh_ui()

    def action_first_trace(self):
        self.current_index = 0
        self.refresh_ui()

    def action_last_trace(self):
        if self.trace_data:
            self.current_index = len(self.trace_data) - 1
            self.refresh_ui()

    def action_jump_forward(self):
        if self.trace_data:
            self.current_index = min(
                self.current_index + 5,
                len(self.trace_data) - 1,
            )
            self.refresh_ui()

    def action_jump_backward(self):
        self.current_index = max(self.current_index - 5, 0)
        self.refresh_ui()

    def action_quit_app(self):
        self.exit()


if __name__ == "__main__":
    PyChronicleApp().run()