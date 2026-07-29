from pychronicle.delta.reconstructor import StateReconstructor


deltas = [
    {"x": 10},
    {"y": 20},
    {"z": 30},
    {"x": 15},
]


reconstructor = StateReconstructor()


print("Full State")
print(reconstructor.reconstruct(deltas))

print("\nState After Step 1")
print(reconstructor.reconstruct_until(deltas, 0))

print("\nState After Step 2")
print(reconstructor.reconstruct_until(deltas, 1))

print("\nState After Step 3")
print(reconstructor.reconstruct_until(deltas, 2))

print("\nState After Step 4")
print(reconstructor.reconstruct_until(deltas, 3))