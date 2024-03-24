class Context:
    def __init__(self, state, root, animator=None):
        self._root = root
        self._animator = animator
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
    
    @property
    def animator(self):
        if self._animator == None:
            raise Exception("Animator is not set")
        return self._animator