from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    def __init__(self, state, root, animator=None):
        self._root = root
        self._animator = animator
        self._state = None
        self.after_id = None
        self.transition_to(state)

    def transition_to(self, state, env={}):
        # exit from previous state
        if self.after_id:
            self._root.after_cancel(self.after_id)
        if self._state:
            self._state.exit()

        # build new state
        self._state = state
        self._state.context = self
        if env == {}:
            self._state.enter()
        else:
            self._state.enter(env)
        # run loop
        self._process()

    def _process(self):
        self._state.update()
        self.after_id = self._root.after(100, self._process) #update rate. make it changeable?

    @property
    def root(self):
        return self._root
    
    @property
    def animator(self):
        if self._animator == None:
            raise Exception("Animator is not set")
        return self._animator
    

class State(ABC):
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context) -> None:
        self._context = context

    @abstractmethod
    def enter(self, env={}) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def exit(self) -> None:
        pass
