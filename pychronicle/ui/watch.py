import ast


WATCH_VARIABLES = [
    "x",
    "y",
    "result",
    "value",
    "sum_result",
    "final_result",
]


def parse_snapshot(snapshot: str) -> dict:
    """
    Convert the stored snapshot string back into a Python dictionary.
    """

    if not snapshot:
        return {}

    try:
        return ast.literal_eval(snapshot)
    except Exception:
        return {}

def build_watch_panel(current_snapshot: str, previous_snapshot: str | None = None) -> str:
    """
    Build the watch variables panel.
    Changed variables are marked with *
    """

    current = parse_snapshot(current_snapshot)
    previous = parse_snapshot(previous_snapshot) if previous_snapshot else {}

    output = ["Watch Variables\n"]

    for variable in WATCH_VARIABLES:

        if variable in current:

            current_value = current[variable]
            previous_value = previous.get(variable)

            changed = current_value != previous_value

            marker = "* " if changed else "  "

            output.append(
                f"{marker}{variable} = {current_value}"
            )

    if len(output) == 1:
        output.append("No watched variables found.")

    return "\n".join(output)