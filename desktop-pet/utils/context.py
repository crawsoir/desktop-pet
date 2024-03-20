class Context:
    def __init__(self, state, root):
        self._root = root
        self._state = state
        self._state.context = self
        self._state.enter()

    def transition_to(self, state):
        self._state.exit()
        self._state = state
        self._state.context = self
        self._state.enter()

    @property
    def root(self):
        return self._root