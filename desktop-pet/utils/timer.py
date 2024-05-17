class TkinterTimer():
    id = None

    def __init__(self, root, time=0):
        self.root = root
        self.time = time
        self.is_stopped = True

    def start(self, time=None):
        print("starting timer: " + str(time))
        if time: 
            self.time = time
        if self.id: 
            self.root.after_cancel(self.id)

        self.id = self.root.after(self.time, self._stopped)
        self.is_stopped = False

    def _stopped(self):
        self.is_stopped = True

    def is_stopped(self):
        return self.is_stopped

    def __exit__(self):
        print("hi!!")
        if self.id:
            self.root.after_cancel(self.id)