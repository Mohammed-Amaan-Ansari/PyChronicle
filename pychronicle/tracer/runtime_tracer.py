import sys
import time

from pychronicle.delta.compressor import DeltaCompressor
from pychronicle.storage.database import insert_execution_trace
from pychronicle.storage.models import ExecutionTrace


compressor = DeltaCompressor()


def is_traceable(frame):
    """
    Trace only user project files.
    Skip Python internals and site-packages.
    """

    filename = frame.f_code.co_filename.replace("\\", "/")

    # Trace only files inside examples or pychronicle
    return (
        "/examples/" in filename
        or "/pychronicle/" in filename
    )


def safe_serialize(value):
    """
    Convert values to safe string representations.
    """

    try:
        repr(value)
        return value
    except Exception:
        return f"<unserializable:{type(value).__name__}>"


def trace_function(frame, event, arg):
    """
    Runtime tracing function using delta compression.
    """

    # Skip non-project files
    if not is_traceable(frame):
        return trace_function

    if event not in ("call", "line", "return"):
        return trace_function

    current_state = {}

    for key, value in frame.f_locals.items():

        if key.startswith("__"):
            continue

        current_state[key] = safe_serialize(value)

    delta = compressor.compress(current_state)

    trace = ExecutionTrace(
        timestamp=time.time(),
        event_type=event,
        line_number=frame.f_lineno,
        function_name=frame.f_code.co_name,
        locals_snapshot=str(delta),
    )

    insert_execution_trace(trace)

    return trace_function


def start_tracing():
    sys.settrace(trace_function)


def stop_tracing():
    sys.settrace(None)