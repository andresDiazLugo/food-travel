import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import os
import uuid
from controllers.controllerUser import ControllerUser
class SignInUser(ctk.CTkFrame):
    def __init__(self,app=None,controller:ControllerUser=None):
        super().__init__(app,fg_color="#03071e")
        self.controller = controller
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory,'assets/img_login.jpg')
        # #crear otro frame
        self.my_image = ctk.CTkImage(light_image=Image.open(file_path),
                                dark_image=Image.open(file_path),
                                size=(600,700)
                                )
        self.content_Frame = ctk.CTkFrame(self,fg_color="#03071e",width=600,height=700)
        self.content_Frame.pack(side=ctk.LEFT)
        self.form_content = ctk.CTkFrame(self,fg_color="#03071e",width=400,height=700)
        self.form_content.pack(expand=True,fill='both')
        self.label_image = ctk.CTkLabel(self.content_Frame,image=self.my_image,text='',width=600,height=700)
        self.label_image.place(x=0, y=0)

        # frame para el formulario
        self.form_content3 = ctk.CTkFrame(self.form_content,fg_color="#03071e",width=700)
        self.form_content3.pack(fill='both',pady=200)
    
        self.label_title =  ctk.CTkLabel(self.form_content3,text='Inicia Sesion', text_color="white",font=ctk.CTkFont(family='Arial',size=25, weight="bold"))
        self.label_title.pack()
        # label y inputs
        self.emailInput = ctk.CTkEntry(self.form_content3,width=300,placeholder_text='ingrese email')
        self.label_email = ctk.CTkLabel(self.form_content3,text='email:', text_color="white")
        self.label_email.pack()
        self.emailInput.pack()
        # 
        self.passwordInput = ctk.CTkEntry(self.form_content3,width=300, placeholder_text='ingrese password')
        self.label_password = ctk.CTkLabel(self.form_content3,text='password:', text_color="white")
        self.label_password.pack()
        self.passwordInput.pack()
        # 
        self.button_register = ctk.CTkButton(self.form_content3, text='Iniciar Sesion',command=self.controller.signin)
        self.button_register.pack(side=ctk.LEFT,pady=10,padx=9)
        self.button_login = ctk.CTkButton(self.form_content3, text='Registrate', command= self.controller.navigate_register)
        self.button_login.pack(side=ctk.RIGHT,pady=10,padx=9)

    def return_data_user(self):
            data= {
                'id':None,
                'nombre' : None,
                'apellido' : None,
                'email': self.emailInput.get(),
                'password': self.passwordInput.get()
            }
            return data
    def meesageError(self,info):
        messagebox.showerror('Error',info)
    def reset_value_camp(self):
        self.emailInput.delete(0,ctk.END)
        self.passwordInput.delete(0,ctk.END)
