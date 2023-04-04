import tkinter as tk

class HomeView(tk.Frame):
    def __init__(self, switch_to_login, master=None):
        super().__init__(master)
        self.master = master
        self.switch_to_login = switch_to_login
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Home")

        self.home_label = tk.Label(self, text=":-)")
        self.home_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.logout_button = tk.Button(self, text="Logout", command=self.logout)  
        self.logout_button.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

    def logout(self): 
        self.pack_forget()
        self.switch_to_login()



        