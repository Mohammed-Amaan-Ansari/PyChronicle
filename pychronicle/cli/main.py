from pathlib import Path
import runpy

import typer

from pychronicle.storage.schema import initialize_database
from pychronicle.tracer.runtime_tracer import start_tracing, stop_tracing


app = typer.Typer(
    help="PyChronicle - AST Powered Time Travel Debugger"
)

@app.command()
def run(script: str):
    """
    Run a Python script under PyChronicle tracing.

    Example:
        pychronicle run examples/final_demo.py
    """

    script_path = Path(script)

    if not script_path.exists():
        typer.echo(f"File not found: {script}")
        raise typer.Exit(code=1)

    typer.echo("Initializing PyChronicle database...")
    initialize_database()

    typer.echo(f"Tracing script: {script_path}")

    try:
        start_tracing()

        runpy.run_path(str(script_path), run_name="__main__")

        typer.echo("✅ Execution completed successfully")

    except Exception as error:
        typer.echo(f"❌ Execution failed: {error}")
        raise typer.Exit(code=1)

    finally:
        stop_tracing()


@app.command()
def ui():
    """
    Launch the PyChronicle Textual UI.
    """

    typer.echo("🖥️ Launching PyChronicle UI...")

    from pychronicle.ui.app import PyChronicleApp

    PyChronicleApp().run()


@app.command()
def version():
    """
    Show the current PyChronicle version.
    """

    typer.echo("PyChronicle v0.1.0")


if __name__ == "__main__":
    app()