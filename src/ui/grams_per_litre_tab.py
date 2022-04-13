from tkinter import ttk, constants

class GramsPerLitreTab:
    def __init__(self, root):
        self._root = root
        self.frame = None
        self.label = "g/L"
        self._initialize()

    def _initialize(self):
        self.frame = ttk.Frame(master=self._root)
