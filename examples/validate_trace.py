from pychronicle.storage.database import get_execution_trace


trace_data = get_execution_trace()


print("Trace Validation Report")
print("-" * 40)


call_count = 0
line_count = 0
return_count = 0

