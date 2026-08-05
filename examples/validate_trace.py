from pychronicle.storage.database import get_execution_trace


trace_data = get_execution_trace()


print("Trace Validation Report")
print("-" * 40)


call_count = 0
line_count = 0
return_count = 0

for trace in trace_data:
    event = trace[1]

    if event == "call":
        call_count += 1
    elif event == "line":
        line_count += 1
    elif event == "return":
        return_count += 1


print(f"Call Events   : {call_count}")
print(f"Line Events   : {line_count}")
print(f"Return Events : {return_count}")
print(f"Total Records : {len(trace_data)}")


if call_count > 0 and return_count > 0:
    print("\n✓ Trace appears valid")
else:
    print("\n✗ Trace validation failed")