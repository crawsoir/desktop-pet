import threading

class Context:
    _state = None
    def __init__(self, state):
        self._state = state
        self._state.context = self
        self._state.enter()
        self._process()

    def transition_to(self, state):
        self._state.exit()
        self._state = state
        self._state.context = self
        self._state.enter()

    def _process(self):
        threading.Timer(1.0, self._process).start()
        self._state.update()
