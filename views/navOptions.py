import customtkinter as ctk
from tkinter import messagebox
from controllers.controllerUser import ControllerUser

class Nav_Options(ctk.CTkFrame):
    def __init__(self,app,controller:ControllerUser,controllerMap):
        super().__init__(app,fg_color='white')
        self.controller = controller
        self.controllerMap = controllerMap
        self.app = app
        self.pack()
    

        self.frame_option= ctk.CTkFrame(self,fg_color='#343a40',width=180,height=700)
        self.frame_option.pack(side=ctk.LEFT)

        # botones para el frame nav options
        boton_destino_culinario = ctk.CTkButton(self.frame_option, text='Destinos',font=('Bold',18),text_color='white',fg_color='#343a40',command=lambda:self.indicate(self.destino_culinario,self.view_map))
        boton_destino_culinario.place(x=20, y=50)
        self.destino_culinario = ctk.CTkLabel(self.frame_option,text='',fg_color='#343a40',width=5,height=30)
        self.destino_culinario.place(x=14,y=50)

        boton_historial = ctk.CTkButton(self.frame_option, text='Historial de rutas',font=('Bold',18),text_color='white',fg_color='#343a40',command=lambda:self.indicate(self.indicate_menu,self.view_history))
        boton_historial.place(x=20, y=100)
        self.indicate_menu = ctk.CTkLabel(self.frame_option,text='',fg_color='#343a40',width=5,height=30)
        self.indicate_menu.place(x=14,y=100)

        boton_review = ctk.CTkButton(self.frame_option, text='Reviews',font=('Bold',18),text_color='white',fg_color='#343a40',command=lambda:self.indicate(self.indicate_calificacion,self.view_about))
        boton_review.place(x=20, y=150)
        self.indicate_calificacion = ctk.CTkLabel(self.frame_option,text='',fg_color='#343a40',width=5,height=30)
        self.indicate_calificacion.place(x=14,y=150)
        
        self.name_user = ctk.CTkLabel(self.frame_option,text=self.controller.session['nombre'] if self.controller.session != None else '',fg_color='#343a40',text_color='white',font=('Bold',18),padx=10, pady=5)
        self.name_user.place(x=30, y=600)
        self.icon_connect = ctk.CTkLabel(self.frame_option,text='',fg_color='#02c39a',font=('Bold',18),width=15,height=15)
        self.icon_connect.place(x=20, y=605)
        boton_cerrar_sesion = ctk.CTkButton(self.frame_option, text='Cerrar Sesion',font=('Bold',18),text_color='white',fg_color='red',command=self.show_message_logout)
        boton_cerrar_sesion.place(x=20, y=650)

        # frame donde se va a renderizar las demas vistas
        self.main_frame = ctk.CTkFrame(self,fg_color='white',width=820,height=700)
        self.main_frame.pack(side=ctk.LEFT)
        self.indicate(self.destino_culinario,self.view_map)
        
        # function of navigate
    def indicate(self,lb,page):
        self.remove_indicate()
        lb.configure(fg_color='orange')
        self.delete_page()
        page()
    def remove_indicate(self):
        self.destino_culinario.configure(fg_color='#343a40')
        self.indicate_menu.configure(fg_color='#343a40')
        self.indicate_calificacion.configure(fg_color='#343a40')
        # views options
    def view_map(self):
         map = self.app.map_view(self.main_frame,self.app,self.controllerMap )
         map.pack(side=ctk.LEFT)
    def view_history(self):
        historial = self.app.history_user_view(self.main_frame,self.app)
        historial.pack(side=ctk.LEFT)
    def view_about(self):
        reviews =  self.app.reviews_views(self.main_frame,self.app)
        reviews.pack(side=ctk.LEFT)
    def delete_page(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()
    def show_message_logout(self):
        response = messagebox.askokcancel("Confirmar", "¿Estás de que quieres cerrar sesion?")
        if response:
            self.controller.navigate_login()
       