import ast
import time

from pychronicle.storage.database import get_execution_trace


def replay_trace(start: int = 1, end: int | None = None, delay: float = 0.5):
    """
    Replay execution trace step by step.
    """

    trace_data = get_execution_trace()

    if not trace_data:
        print("No trace data available.")
        return

    total = len(trace_data)

    start_index = max(start - 1, 0)
    end_index = total if end is None else min(end, total)

    print("PyChronicle Trace Replay")
    print("=" * 40)

    current_state = {}

    for step, trace in enumerate(trace_data[start_index:end_index], start=start):
        event_type = trace[1]
        line_number = trace[2]
        function_name = trace[3]
        snapshot = trace[4]

        # Apply delta snapshot
        try:
            delta = ast.literal_eval(snapshot)

            if isinstance(delta, str):
                delta = ast.literal_eval(delta)

            if isinstance(delta, dict):
                current_state.update(delta)

        except Exception:
            pass

        print(f"\nStep {step}")
        print("-" * 20)
        print(f"Event    : {event_type}")
        print(f"Function : {function_name}")
        print(f"Line     : {line_number}")

        print("State")

        if current_state:
            for key, value in current_state.items():
                print(f"  {key} = {value}")
        else:
            print("  <empty>")

        time.sleep(delay)