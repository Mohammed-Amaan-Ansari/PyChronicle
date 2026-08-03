import ast
import copy


class StateReconstructor:
    """
    Rebuilds complete state from delta snapshots.
    """

    def reconstruct_until(self, trace_data, index: int):

        state = {}

        for trace in trace_data[: index + 1]:

            snapshot = trace[4]

            if not snapshot:
                continue

            try:
                delta = ast.literal_eval(snapshot)

                if isinstance(delta, str):
                    delta = ast.literal_eval(delta)

                if isinstance(delta, dict):
                    state.update(delta)

            except Exception:
                continue

        return copy.deepcopy(state)