import json
from pathlib import Path

from pychronicle.storage.database import get_execution_trace


def export_trace_to_json(output_file: str):
    """
    Export execution trace to a JSON file.
    """

    trace_data = get_execution_trace()

    export_data = []

    for trace in trace_data:
        export_data.append({
            "timestamp": trace[0],
            "event_type": trace[1],
            "line_number": trace[2],
            "function_name": trace[3],
            "locals_snapshot": trace[4],
        })

    output_path = Path(output_file)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(export_data, file, indent=4)

    return output_path