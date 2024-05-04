class Context:

    def __init__(self, state, root, animator=None):
        self._root = root
        self._animator = animator
        self._state = None
        self.transition_to(state)

    def transition_to(self, state, env={}):
        if self._state:
            self._state.exit()
        self._state = state
        self._state.context = self
        if env == {}:
            self._state.enter()
        else:
            self._state.enter(env)
        self._process()

    def _process(self):
        self._state.update()
        self._root.after(100, self._process) #fps rate. make it changeable? TODO: need to cancel repeated processes

    @property
    def root(self):
        return self._root
    
    @property
    def animator(self):
        if self._animator == None:
            raise Exception("Animator is not set")
        return self._animator