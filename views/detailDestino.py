import customtkinter as ctk
from controllers.controllerMap import Controller_Map
from PIL import Image
import os
class DetailDestino(ctk.CTkToplevel):
    def __init__(self,app,destino_id,data_detail):
        super().__init__(app,fg_color='#495057')
        self.destino_id = destino_id
        self.title('Detalles de destino')
        window_width, window_height = 300, 450
        self.resizable(False,False)
        self.window_center(window_width,window_height)
        self.attributes("-topmost", True)
        self.data_detail = data_detail
        label_nombre = ctk.CTkLabel(self,text="Nombre:",font=('Bold',18))
        label_nombre_value = ctk.CTkLabel(self,text=self.data_detail['nombre'],font=('Bold',18))
        label_nombre.place(x=0,y=50)
        label_nombre_value.place(x=90,y=50)
        
        label_tipo = ctk.CTkLabel(self,text="Tipo de cocina:",font=('Bold',18))
        label_tipo_value = ctk.CTkLabel(self,text=self.data_detail['tipo_cocina'],font=('Bold',18))
        label_tipo.place(x=0,y=75)
        label_tipo_value.place(x=145,y=75)

        label_precio_max = ctk.CTkLabel(self,text="Precio Maximo:",font=('Bold',18))
        label_precio_max_value = ctk.CTkLabel(self,text=data_detail['precio_maximo'],font=('Bold',18))
        label_precio_max.place(x=0,y=100)
        label_precio_max_value.place(x=145,y=100)


        label_precio_min = ctk.CTkLabel(self,text="Precio Minimo:",font=('Bold',18))
        label_precio_min_value = ctk.CTkLabel(self,text=data_detail['precio_minimo'],font=('Bold',18))
        label_precio_min.place(x=0,y=125)
        label_precio_min_value.place(x=143,y=125)

        label_popularidad= ctk.CTkLabel(self,text="Popularidad:",font=('Bold',18))
        label_popularidad_value = ctk.CTkLabel(self,text=data_detail['popularidad'],font=('Bold',18))
        label_popularidad.place(x=0,y=150)
        label_popularidad_value.place(x=127,y=150)


        label_disponibilidad= ctk.CTkLabel(self,text="Disponibilidad:",font=('Bold',18))
        label_disponibilidad_value = ctk.CTkLabel(self,text='Disponible' if data_detail['popularidad'] else 'No Disponible' ,font=('Bold',18))
        label_disponibilidad.place(x=0,y=175)
        label_disponibilidad_value.place(x=139,y=175)


        current_directory = os.getcwd()
        file_path = os.path.join(current_directory,data_detail['imagen'])
        self.my_image = ctk.CTkImage(light_image=Image.open(file_path),
                                dark_image=Image.open(file_path),
                                size=(300,300)
                                )
        
        self.label_image = ctk.CTkLabel(self,image=self.my_image,text='',width=300)
        self.label_image.place(x=0, y=200)

        label_ingredientes= ctk.CTkLabel(self,text="Ingredientes")

        



        
    def window_center(self, w, h):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (w // 2)
        y = (screen_height // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")