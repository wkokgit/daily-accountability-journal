from tkinter import Tk

DEFAULT_FONT = "Verdana"

class Frame():
    def __init__(self):
        self.root = Tk()
        self.root.option_add("*Font", DEFAULT_FONT)

