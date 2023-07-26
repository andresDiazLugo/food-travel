import customtkinter as ctk
class RegisterUser(ctk.CTkFrame):
    def __init__(self,app=None,controller=None):
        super().__init__(app)
        self.controller = controller
        button = ctk.CTkButton(self, text='registro',command=lambda: print('Hola mundo'))
        button.pack()