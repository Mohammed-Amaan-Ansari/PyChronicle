import ast
import time

from pychronicle.storage.database import get_execution_trace


def replay_trace(
    start: int = 1,
    end: int | None = None,
    delay: float = 0.5,
    breakpoint_line: int | None = None,
    interactive: bool = False,
):
    """
    Replay execution trace step by step.
    Supports breakpoints and interactive stepping.
    """

    trace_data = get_execution_trace()

    if not trace_data:
        print("No trace data available.")
        return

    total = len(trace_data)

    start_index = max(start - 1, 0)
    end_index = total if end is None else min(end, total)

    print("PyChronicle Interactive Replay")
    print("=" * 50)

    if breakpoint_line:
        print(f"🎯 Breakpoint set at line {breakpoint_line}")

    if interactive:
        print("🕹️ Interactive mode enabled")
        print("Press Enter to step, 'c' to continue, 'q' to quit")

    current_state = {}
    continue_mode = False

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
        print("-" * 30)
        print(f"Event    : {event_type}")
        print(f"Function : {function_name}")
        print(f"Line     : {line_number}")

        print("State")

        if current_state:
            for key, value in current_state.items():
                print(f"  {key} = {value}")
        else:
            print("  <empty>")

        # Breakpoint handling
        if breakpoint_line and line_number == breakpoint_line:
            print(f"\n⛔ Breakpoint hit at line {line_number}")

            while True:
                command = input("(pychronicle) [s]tep/[c]ontinue/[q]uit: ").strip().lower()

                if command in ("s", ""):
                    break
                elif command == "c":
                    continue_mode = True
                    break
                elif command == "q":
                    print("🛑 Replay terminated by user")
                    return

        # Interactive stepping
        if interactive and not continue_mode:
            command = input("(pychronicle) Press Enter to continue, 'c' for continuous, 'q' to quit: ").strip().lower()

            if command == "c":
                continue_mode = True
            elif command == "q":
                print("🛑 Replay terminated by user")
                return

        if not interactive and not continue_mode:
            time.sleep(delay)

    print("\n✅ Replay completed successfully")