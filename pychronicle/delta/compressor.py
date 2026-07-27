import copy


class DeltaCompressor:
    """
    Computes the difference (delta) between two execution states.
    """

    def __init__(self):
        # Stores the previous complete state
        self.previous_state = {}

    def compress(self, current_state: dict) -> dict:
        """
        Return only the variables that changed.
        """

        delta = {}

        for variable, value in current_state.items():

            if variable not in self.previous_state:
                delta[variable] = value

            elif self.previous_state[variable] != value:
                delta[variable] = value

        # Save current state for the next comparison
        self.previous_state = copy.deepcopy(current_state)

        return delta