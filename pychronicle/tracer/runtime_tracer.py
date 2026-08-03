import sys
import time

from pychronicle.delta.compressor import DeltaCompressor
from pychronicle.storage.database import insert_execution_trace
from pychronicle.storage.models import ExecutionTrace


compressor = DeltaCompressor()


def trace_function(frame, event, arg):
    """
    Runtime tracing function using delta compression.
    """

    if event not in ("call", "line", "return"):
        return trace_function

    current_state = {
        key: value
        for key, value in frame.f_locals.items()
        if not key.startswith("__")
    }

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