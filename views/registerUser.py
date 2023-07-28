import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import os
import uuid
from controllers.controllerUser import ControllerUser
class RegisterUser(ctk.CTkFrame):
    def __init__(self,app=None,controller:ControllerUser=None):
        super().__init__(app,fg_color="#03071e")
        self.controller = controller
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory,'assets/img_inicio.jpg')
        # #crear otro frame
        my_image = ctk.CTkImage(light_image=Image.open(file_path),
                                dark_image=Image.open(file_path),
                                size=(600,700)
                                )
        content_Frame = ctk.CTkFrame(self,fg_color="#03071e",width=600,height=700)
        content_Frame.pack(side=ctk.LEFT)
        form_content = ctk.CTkFrame(self,fg_color="#03071e",width=400,height=700)
        form_content.pack(expand=True,fill='both')
        label_image = ctk.CTkLabel(content_Frame,image=my_image,text='',width=600,height=700)
        label_image.place(x=0, y=0)

        # frame para el formulario
        form_content3 = ctk.CTkFrame(form_content,fg_color="#03071e",width=700)
        form_content3.pack(fill='both',pady=200)
    
        label_title =  ctk.CTkLabel(form_content3,text='Registrate en el sistema', text_color="white",font=ctk.CTkFont(family='Arial',size=25, weight="bold"))
        label_title.pack()
        # label y inputs
        self.nameInput = ctk.CTkEntry(form_content3,width=300,placeholder_text="ingrese nombre")
        label_name = ctk.CTkLabel(form_content3,text='Nombre :', text_color="white")
        label_name.pack()
        self.nameInput.pack()
        # 
        self.apellidoInput = ctk.CTkEntry(form_content3,width=300,placeholder_text="ingrese apellido")
        label_APELLIDO = ctk.CTkLabel(form_content3,text='Apellido:', text_color="white")
        label_APELLIDO.pack()
        self.apellidoInput.pack()
        # 
        self.emailInput = ctk.CTkEntry(form_content3,width=300,placeholder_text='ingrese email')
        label_email = ctk.CTkLabel(form_content3,text='email:', text_color="white")
        label_email.pack()
        self.emailInput.pack()
        # 
        self.passwordInput = ctk.CTkEntry(form_content3,width=300, placeholder_text='ingrese password')
        label_password = ctk.CTkLabel(form_content3,text='password:', text_color="white")
        label_password.pack()
        self.passwordInput.pack()
        # 
        button_register = ctk.CTkButton(form_content3, text='Registrar',command=self.controller.register_user)
        button_register.pack(side=ctk.LEFT,pady=10,padx=9)
        button_login = ctk.CTkButton(form_content3, text='Iniciar Sesion',command=self.controller.navigate_login)
        button_login.pack(side=ctk.RIGHT,pady=10,padx=9)

    def return_data_user(self):
            id_uniq = str(uuid.uuid4())
            data= {
                'id':id_uniq,
                'nombre' : self.nameInput.get(),
                'apellido' : self.apellidoInput.get(),
                'email': self.emailInput.get(),
                'password': self.passwordInput.get()
            }
            return data
    def meesageError(self,info):
        messagebox.showerror('Error',info)
    def messageSuccess(self):
         messagebox.showinfo('Éxito','Tu cuenta fue registrada con exito, inicia sesion')



    
        
        
        # button = ctk.CTkButton(self,fg_color='#FF00FF', text='registro',command=self.controller.register_user)
    
