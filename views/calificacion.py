import customtkinter as ctk
import uuid
from tkinter import messagebox
class Calificacion(ctk.CTkToplevel):
    def __init__(self,app,destino_id,main):
        super().__init__(app,fg_color='orange')
        self.main = main
        self.destino_id = destino_id
        self.title('Detalles de destino')
        window_width, window_height = 500, 360
        self.resizable(False,False)
        self.window_center(window_width,window_height)
        self.attributes("-topmost", True)
        self.estado_anonimo = ctk.BooleanVar
        
        label_comentario= ctk.CTkLabel(self,text="Comentario:",font=('Bold',18))
        self.text_comentario = ctk.CTkTextbox(self,width=300)
        label_comentario.place(x=10,y=10)
        self.text_comentario.place(x=135,y=10)
        
        
        label_calificacion = ctk.CTkLabel(self,text='Califique:',font=('Bold',18))
        self.dorpdown_calificacion = ctk.CTkOptionMenu(self,values=['1 estrellas' ,'2 estrellas','3 estrellas','4 estrellas', '5 estrellas'],fg_color='#212529')
        label_calificacion.place(x=10,y=220)
        self.dorpdown_calificacion.place(x=100,y=220)
        
        self.checkbox_anonimo = ctk.CTkCheckBox(self,text='Modo Anonimo')
        self.checkbox_anonimo.place(x=300,y=220)
        
        self.button_calificar = ctk.CTkButton(self,text='Calificar',font=('Bold',15),text_color='white',command=self.save_calificacion)
        self.button_calificar.place(x=180, y=280)

        
    def window_center(self, w, h):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (w // 2)
        y = (screen_height // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")
    def return_data_calificacion(self):
            id_uniq = str(uuid.uuid4())
            sesion_id = self.main.user_controller.session['id']
            data= {
                'id':id_uniq,
                'id_destino' : self.destino_id,
                'id_usuario' : sesion_id,
                'calificacion': self.dorpdown_calificacion.get(),
                'comentario': self.text_comentario.get("1.0", "end-1c"),
                'anonimo': self.checkbox_anonimo.get()
            }
            return data
    def save_calificacion(self):
        data = self.return_data_calificacion()
        confirm_save = self.main.calificacion_controller.save_calificacion(data)
        if confirm_save:
              self.destroy()
              messagebox.showinfo('Éxito','Tu opinion fue registrada')
        else:
              self.destroy()
              messagebox.showerror('Error','Hubo un error al querer registrar tu opinion')
             