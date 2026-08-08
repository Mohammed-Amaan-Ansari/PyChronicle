from pathlib import Path
import runpy

import typer

from pychronicle.exporter.json_exporter import export_trace_to_json
from pychronicle.session.manager import SessionManager
from pychronicle.storage.schema import initialize_database
from pychronicle.tracer.runtime_tracer import start_tracing, stop_tracing
from pychronicle.analytics.report import format_statistics_report

app = typer.Typer( help="PyChronicle - AST Powered Time Travel Debugger")


@app.command()
def run(script: str):
    """
    Run a Python script under PyChronicle tracing.
    """

    script_path = Path(script)

    if not script_path.exists():
        typer.echo(f"❌ File not found: {script}")
        raise typer.Exit(code=1)

    session = SessionManager()
    info = session.get_session_info()

    typer.echo("🚀 Initializing PyChronicle database...")
    initialize_database()

    typer.echo(f"🆔 Session ID : {info['session_id']}")
    typer.echo(f"🕒 Started    : {info['started_at']}")
    typer.echo(f"📄 Script     : {script_path}")

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
def export(output: str = typer.Argument("trace_report.json")):
    """
    Export the current execution trace to JSON.
    """

    try:
        output_path = export_trace_to_json(output)
        typer.echo(f"📦 Trace exported to: {output_path}")

    except Exception as error:
        typer.echo(f"❌ Export failed: {error}")
        raise typer.Exit(code=1)


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

    typer.echo("PyChronicle v0.2.0")

@app.command()
def stats():
    """
    Show execution trace statistics.
    """

    typer.echo(format_statistics_report())


if __name__ == "__main__":
    app()