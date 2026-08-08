from pychronicle.analytics.trace_stats import generate_trace_statistics


def format_statistics_report() -> str:
    """
    Create a formatted analytics report.
    """

    stats = generate_trace_statistics()

    if stats["total_records"] == 0:
        return "No trace data available."

    lines = []

    lines.append("PyChronicle Trace Statistics")
    lines.append("=" * 40)

    lines.append(f"Total Trace Records : {stats['total_records']}")
    lines.append("")

    lines.append("Event Counts")
    lines.append("-" * 20)

    for event, count in stats["event_counts"].items():
        lines.append(f"{event:<10} : {count}")

    lines.append("")
    lines.append("Function Calls")
    lines.append("-" * 20)

    for function, count in stats["function_calls"].items():
        lines.append(f"{function:<20} : {count}")

    lines.append("")
    lines.append("Most Executed Lines")
    lines.append("-" * 20)

    for line, count in stats["line_frequency"].items():
        lines.append(f"Line {line:<4} : {count} executions")

    lines.append("")

    if stats["most_active_function"]:
        function, count = stats["most_active_function"]
        lines.append(f"Most Active Function : {function} ({count} calls)")

    return "\n".join(lines)