import copy


class StateReconstructor:
    """
    Rebuilds the complete program state from a sequence of deltas.
    """

    def reconstruct(self, deltas: list[dict]) -> dict:
        """
        Apply all deltas in order and return the final state.
        """

        state = {}

        for delta in deltas:
            state.update(delta)

        return copy.deepcopy(state)

    def reconstruct_until(self, deltas: list[dict], index: int) -> dict:
        """
        Reconstruct the state up to a specific delta index.

        Example:
            index = 2
            applies deltas[0], deltas[1], deltas[2]
        """

        state = {}

        for delta in deltas[: index + 1]:
            state.update(delta)

        return copy.deepcopy(state)