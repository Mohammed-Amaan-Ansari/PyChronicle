from pychronicle.storage.database import get_execution_trace


for trace in get_execution_trace():
    print(trace)