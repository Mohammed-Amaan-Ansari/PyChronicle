import sys
import time
from pathlib import Path

from pychronicle.delta.compressor import DeltaCompressor
from pychronicle.storage.database import insert_execution_trace
from pychronicle.storage.models import ExecutionTrace


compressor = DeltaCompressor()


ALLOWED_FUNCTIONS = {
    "calculate_total",
    "apply_discount",
    "generate_report",
}


def trace_function(frame, event, arg):
    """Trace only user business functions."""

    filename = Path(frame.f_code.co_filename).name
    function_name = frame.f_code.co_name

    # Trace only final_demo.py
    if filename != "final_demo.py":
        return trace_function

    # Trace only important functions
    if function_name not in ALLOWED_FUNCTIONS:
        return trace_function

    # Keep only useful events
    if event not in ("call", "line", "return"):
        return trace_function

    current_state = {}

    for key, value in frame.f_locals.items():

        if key.startswith("__"):
            continue

        if isinstance(value, (int, float, str, bool, list, tuple)):
            current_state[key] = value

    delta = compressor.compress(current_state)

    # Skip empty line events
    if event == "line" and not delta:
        return trace_function

    trace = ExecutionTrace(
        timestamp=round(time.time(), 3),
        event_type=event,
        line_number=frame.f_lineno,
        function_name=function_name,
        locals_snapshot=str(delta),
    )

    insert_execution_trace(trace)

    return trace_function


def start_tracing():
    sys.settrace(trace_function)


def stop_tracing():
    sys.settrace(None)