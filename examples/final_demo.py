from pychronicle.tracer.runtime_tracer import start_tracing, stop_tracing


def calculate_total(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


def apply_discount(amount, percentage):
    discount = amount * percentage / 100
    final_amount = amount - discount

    return final_amount


def generate_report(values):
    subtotal = calculate_total(values)
    payable = apply_discount(subtotal, 10)

    return payable


start_tracing()

items = [100, 200, 300, 400]
result = generate_report(items)

stop_tracing()

print(f"Final Result: {result}")