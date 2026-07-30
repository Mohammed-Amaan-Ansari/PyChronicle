# from pychronicle.storage.database import get_execution_trace


# def load_trace():

#     rows = get_execution_trace()

#     return rows

from pychronicle.storage.database import get_execution_trace


def load_trace():
    return get_execution_trace()
