import csv
from pathlib import Path

from pychronicle.storage.database import get_execution_trace


def export_trace_to_csv(output_file: str):
    """
    Export execution trace to CSV.
    """

    trace_data = get_execution_trace()

    output_path = Path(output_file)

    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "timestamp",
            "event_type",
            "line_number",
            "function_name",
            "locals_snapshot",
        ])

        for trace in trace_data:
            writer.writerow(trace)

    return output_path