import ast
import copy


class StateReconstructor:
    """
    Rebuilds the complete program state from
    delta snapshots stored in the execution trace.
    """

    def reconstruct_until(self, trace_data, index: int):
        state = {}

        # Process all trace records up to the requested index
        for trace in trace_data[: index + 1]:
            snapshot = trace[4]

            # Skip empty snapshots
            if not snapshot or snapshot == "{}":
                continue

            try:
                # Convert string representation back to Python object
                delta = ast.literal_eval(snapshot)

                # Handle nested string snapshots if present
                if isinstance(delta, str):
                    delta = ast.literal_eval(delta)

                # Merge changed variables into the current state
                if isinstance(delta, dict):
                    state.update(delta)

            except Exception:
                # Ignore malformed snapshots
                continue

        # Return a safe copy of the reconstructed state
        return copy.deepcopy(state)