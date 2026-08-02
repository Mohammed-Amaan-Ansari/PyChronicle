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
