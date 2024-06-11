class TkinterTimer():
    """Basically threading.timer, but threading isnt supported in tkinter."""

    def __init__(self, root, time=0):
        self.id = None
        self.root = root
        self.time = time
        self.is_stopped = True

    def start(self, time=None):
        if time: 
            self.time = time
        if self.id: 
            self.root.after_cancel(self.id)

        self.id = self.root.after(self.time, self._timer_just_stopped)
        self.is_stopped = False

    def _timer_just_stopped(self):
        self.is_stopped = True

    def is_stopped(self):
        return self.is_stopped