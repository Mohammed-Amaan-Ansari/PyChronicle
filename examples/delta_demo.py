from pychronicle.delta.compressor import DeltaCompressor

compressor = DeltaCompressor()

states = [
    {"x": 10},
    {"x": 10, "y": 20},
    {"x": 10, "y": 20, "z": 30},
    {"x": 10, "y": 20, "z": 30},
    {"x": 15, "y": 20, "z": 30},
]

for index, state in enumerate(states, start=1):

    delta = compressor.compress(state)

    print(f"State {index}")
    print("Current State :", state)
    print("Delta         :", delta)
    print("-" * 40)