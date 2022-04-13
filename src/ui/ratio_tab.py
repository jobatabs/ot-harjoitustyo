from tkinter import ttk, constants

class RatioTab:
    def __init__(self, root):
        self._root = root
        self.frame = None
        self.label = "1:X"
        self._initialize()

    def _initialize(self):
        self.frame = ttk.Frame(master=self._root)
