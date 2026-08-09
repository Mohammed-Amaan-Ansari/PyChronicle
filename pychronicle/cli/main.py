from pathlib import Path
import runpy

import typer

from pychronicle.exporter.json_exporter import export_trace_to_json
from pychronicle.session.manager import SessionManager
from pychronicle.storage.schema import initialize_database
from pychronicle.tracer.runtime_tracer import start_tracing, stop_tracing
from pychronicle.analytics.report import format_statistics_report
from pychronicle.exporter.csv_exporter import export_trace_to_csv
from pychronicle.search.trace_search import (
    search_by_event,
    search_by_function,
    search_by_line,
    format_trace_results,
)
from pychronicle.replay.player import replay_trace
from pychronicle.session.registry import save_session_record, list_sessions
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
    save_session_record(info["session_id"], str(script_path))

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


@app.command()
def export_csv(output: str = typer.Argument("trace_report.csv")):
    """
    Export execution trace to CSV.
    """

    output_path = export_trace_to_csv(output)
    typer.echo(f"📄 CSV exported to: {output_path}")


@app.command()
def search(
    function: str | None = typer.Option(None, "--function", help="Filter by function name"),
    event: str | None = typer.Option(None, "--event", help="Filter by event type"),
    line: int | None = typer.Option(None, "--line", help="Filter by line number"),
):
    """
    Search execution trace records.
    """

    if function:
        results = search_by_function(function)
        typer.echo(format_trace_results(results))
        return

    if event:
        results = search_by_event(event)
        typer.echo(format_trace_results(results))
        return

    if line is not None:
        results = search_by_line(line)
        typer.echo(format_trace_results(results))
        return

    typer.echo("Please provide --function, --event, or --line")

@app.command()
def replay(
    from_step: int = typer.Option(1, "--from-step", help="Starting step number"),
    to_step: int | None = typer.Option(None, "--to-step", help="Ending step number"),
    delay: float = typer.Option(0.5, "--delay", help="Delay between steps in seconds"),
    breakpoint: int | None = typer.Option(None, "--breakpoint", help="Pause when this line number is reached"),
    interactive: bool = typer.Option(False, "--interactive", help="Enable interactive stepping mode"),
):
    """
    Replay execution trace step by step.
    Supports breakpoints and interactive stepping.
    """

    replay_trace(
        start=from_step,
        end=to_step,
        delay=delay,
        breakpoint_line=breakpoint,
        interactive=interactive,
    )

@app.command()
def sessions():
    """
    List saved tracing sessions.
    """

    session_list = list_sessions()

    if not session_list:
        typer.echo("No saved sessions found.")
        return

    typer.echo("Saved Sessions")
    typer.echo("=" * 30)

    for session_id in session_list:
        typer.echo(f"• {session_id}")

if __name__ == "__main__":
    app()