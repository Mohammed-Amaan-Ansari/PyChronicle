from pathlib import Path
import runpy

import typer

from pychronicle.storage.schema import initialize_database
from pychronicle.tracer.runtime_tracer import start_tracing, stop_tracing


app = typer.Typer(
    help="PyChronicle - AST Powered Time Travel Debugger"
)