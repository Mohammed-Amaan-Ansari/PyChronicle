# from pychronicle.storage.database import get_execution_trace


# def load_trace():

#     rows = get_execution_trace()

#     return rows

from pychronicle.storage.database import get_execution_trace


def load_trace():
    """
    Safely load execution trace data.
    """

    try:
        return get_execution_trace()
    except Exception as error:
        print(f"Error loading trace: {error}")
        return []
