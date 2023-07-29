import customtkinter as ctk

class Home(ctk.CTkButton):
    def __init__(self,app):
        super().__init__(app,fg_color='green')
        self.button_Home = ctk.CTkButton(self, text='Bienvenido al home')
        self.button_Home.grid(row=0,column=0)