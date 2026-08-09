from pychronicle.storage.database import get_execution_trace


def search_by_function(function_name: str):
    """
    Return trace records for a specific function.
    """

    return [
        trace
        for trace in get_execution_trace()
        if trace[3] == function_name
    ]


def search_by_event(event_type: str):
    """
    Return trace records for a specific event type.
    """

    return [
        trace
        for trace in get_execution_trace()
        if trace[1] == event_type
    ]


def search_by_line(line_number: int):
    """
    Return trace records for a specific line number.
    """

    return [
        trace
        for trace in get_execution_trace()
        if trace[2] == line_number
    ]


def format_trace_results(results):
    """
    Format trace records for CLI display.
    """

    if not results:
        return "No matching trace records found."

    lines = []

    for index, trace in enumerate(results, start=1):
        lines.append(f"[{index}]")
        lines.append(f"Event    : {trace[1]}")
        lines.append(f"Function : {trace[3]}")
        lines.append(f"Line     : {trace[2]}")
        lines.append(f"State    : {trace[4]}")
        lines.append("-" * 40)

    return "\n".join(lines)