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
        self.my_image = ctk.CTkImage(light_image=Image.open(file_path),
                                dark_image=Image.open(file_path),
                                size=(600,700)
                                )
        self.content_Frame = ctk.CTkFrame(self,fg_color="#03071e",width=600,height=700)
        self.content_Frame.pack(side=ctk.LEFT)
        self.form_content = ctk.CTkFrame(self,fg_color="#03071e")
        self.form_content.pack(expand=True, pady=40)
        self.label_image = ctk.CTkLabel(self.content_Frame,image=self.my_image,text='',width=600,height=700)
        self.label_image.place(x=0, y=0)
    
        self.label_title =  ctk.CTkLabel(self.form_content,text='Registrate en el sistema', text_color="white",font=ctk.CTkFont(family='Arial',size=25, weight="bold"))
        self.label_title.pack()
        # label y inputs
        self.nameInput = ctk.CTkEntry( self.form_content,width=300,placeholder_text="ingrese nombre")
        self.label_name = ctk.CTkLabel( self.form_content,text='Nombre :', text_color="white")
        self.label_name.pack()
        self.nameInput.pack()
        # 
        self.apellidoInput = ctk.CTkEntry( self.form_content,width=300,placeholder_text="ingrese apellido")
        self.label_APELLIDO = ctk.CTkLabel( self.form_content,text='Apellido:', text_color="white")
        self.label_APELLIDO.pack()
        self.apellidoInput.pack()
        # 
        self.emailInput = ctk.CTkEntry( self.form_content,width=300,placeholder_text='ingrese email')
        self.label_email = ctk.CTkLabel( self.form_content,text='email:', text_color="white")
        self.label_email.pack()
        self.emailInput.pack()
        # 
        bullet = "\u2022"
        self.passwordInput = ctk.CTkEntry( self.form_content,width=300,show=bullet, placeholder_text='ingrese password')
        self.label_password = ctk.CTkLabel( self.form_content,text='password:', text_color="white")
        self.label_password.pack()
        self.passwordInput.pack()
        # 
        self.button_register = ctk.CTkButton( self.form_content, text='Registrar',command=self.controller.register_user)
        self.button_register.pack(side=ctk.LEFT,pady=14,padx=9)
        self.button_login = ctk.CTkButton( self.form_content, text='Iniciar Sesion',command=self.controller.navigate_login)
        self.button_login.pack(side=ctk.RIGHT,pady=14,padx=9)

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
    def reset_value_camp(self):
        self.nameInput.delete(0,ctk.END)
        self.apellidoInput.delete(0,ctk.END)
        self.emailInput.delete(0,ctk.END)
        self.passwordInput.delete(0,ctk.END)




    
        
        
        # button = ctk.CTkButton(self,fg_color='#FF00FF', text='registro',command=self.controller.register_user)
    
