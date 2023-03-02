import tkinter as tk
from .pages.LoginScreen import LoginScreen


class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Example App")
        self.geometry("800x600")

    def startApp(self):
        LoginScreen(self)

        self.mainloop()
