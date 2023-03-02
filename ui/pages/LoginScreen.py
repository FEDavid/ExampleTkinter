import tkinter as tk
from api.login import login


class LoginScreen(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.pack(fill="both", expand=True)

        label = tk.Label(self, text="Login Screen")
        label.grid(row=0, column=0, columnspan=2, ipady=10, sticky='w')
        label.pack()

        username = tk.Entry(self)
        username.pack()

        password = tk.Entry(self)
        password.pack()

        loginButton = tk.Button(
            self, text="Login", command=lambda: login(username.get(), password.get()))
        loginButton.pack()
