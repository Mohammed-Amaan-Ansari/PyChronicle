from collections import Counter

from pychronicle.storage.database import get_execution_trace


def generate_trace_statistics():
    """
    Generate execution trace statistics.
    """

    trace_data = get_execution_trace()

    if not trace_data:
        return {
            "total_records": 0,
            "function_calls": {},
            "line_frequency": {},
            "event_counts": {},
            "most_active_function": None,
        }

    function_counter = Counter()
    line_counter = Counter()
    event_counter = Counter()

    for trace in trace_data:
        event_type = trace[1]
        line_number = trace[2]
        function_name = trace[3]

        event_counter[event_type] += 1
        line_counter[line_number] += 1

        if event_type == "call":
            function_counter[function_name] += 1

    most_active = None

    if function_counter:
        most_active = function_counter.most_common(1)[0]

    return {
        "total_records": len(trace_data),
        "function_calls": dict(function_counter),
        "line_frequency": dict(line_counter.most_common(5)),
        "event_counts": dict(event_counter),
        "most_active_function": most_active,
    }