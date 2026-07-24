from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Static


class PyChronicleApp(App):

    CSS_PATH = "app.tcss"

    TITLE = "PyChronicle"
    SUB_TITLE = "Time Travel Debugger"

    def compose(self) -> ComposeResult:

        yield Header()

        with Container(id="body"):

            yield Static(
                "📄 Code Viewer",
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