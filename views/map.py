import customtkinter as ctk
import tkintermapview as tkmap
import tkinter
from PIL import Image,ImageTk
import os
from controllers.controllerMap import Controller_Map
from views.listofubicaciones import ScrollableLabelButtonFrame
from tkinter import messagebox
class Map(ctk.CTkFrame):
    def __init__(self,app,viewMain,controllermap:Controller_Map | None = None):
        super().__init__(app,width=820,fg_color='orange',height=700)
        
        self.app = app
        self.controllerMap = controllermap
        self.list_path = []
        self.list_destinos_culinarios = viewMain.destinos_culinarios
        self.viewMain = viewMain
        self.state_check_precio = ctk.StringVar()
        self.opcion_dropdown = ctk.StringVar()
        # barra header aca contendremos lo widgets de busqueda, filtros etc
        self.frame_header = ctk.CTkFrame(self,width=820,height=210,fg_color='#a9d6e5')
        self.frame_header.pack(side=ctk.TOP)
        #aca colocaremos los widgets
        self.search_entry = ctk.CTkEntry(self.frame_header,width=250,placeholder_text="Buscar destino clulinario")
        self.search_entry.place(x=56, y=30)
        
        self.button_search = ctk.CTkButton(self.frame_header,text='Buscar',font=('Bold',15),text_color='white',fg_color='orange',command=self.add_element_scrollLaber)
        self.button_search.place(x=188, y=120)
        
        self.checkbox_precio_menor = ctk.CTkRadioButton(self.frame_header,font=('Bold',15), text='precio menor',variable=self.state_check_precio,value='precio menor',fg_color='orange')
        self.checkbox_precio_menor.place(x=60,y=80)
        self.checkbox_precio_mayor = ctk.CTkRadioButton(self.frame_header, text='precio mayor',variable=self.state_check_precio,value='precio mayor',fg_color='orange')
        self.checkbox_precio_mayor.place(x=200,y=80)
        
        self.dorpdown_options = ctk.CTkOptionMenu(self.frame_header,values=["Todos","Regional", "Hindu", "Mediterranea","Japonesa","Canadiense","Mexicana"],fg_color='orange')
        self.dorpdown_options.place(x=30,y=120)
        
        
        #listbox para mostrar los destinos
        self.ScrollableLabelButtonFrame = ScrollableLabelButtonFrame(self.frame_header,width=440, fg_color='orange')
        self.ScrollableLabelButtonFrame.place(x=359,y=0)
        self.frame_map =ctk.CTkFrame(self,width=820,height=490,fg_color='blue')
        self.frame_map.pack(side=ctk.TOP)
        #aca colocaremos el widget mapa
        self.map_widget = tkmap.TkinterMapView(self.frame_map,width=820,height=490,corner_radius=0)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=18) 
        self.map_widget.set_zoom(18)
        self.add_element_scrollLaber()
     
        # aca colocaremos el frame que contendra el mapa
    def add_element_scrollLaber(self):
            self.controllerMap.add_list(self.list_destinos_culinarios)
            precio = self.state_check_precio.get()
            input_entry = self.search_entry.get()
            type_food = self.dorpdown_options.get()
            lista_u = self.controllerMap.filterDestinos(precio,input_entry,type_food)
            self.ScrollableLabelButtonFrame.remove_item()
            
            if len(lista_u) > 0 :
                for destino in lista_u:
                    current_directory = os.getcwd()
                    file_path = os.path.join(current_directory,destino.imagen)
                    plane_image = ImageTk.PhotoImage(Image.open(file_path).resize((120, 120)))
                    location = self.controllerMap.add_location_map(destino.id_ubicacion)
                    marker = self.map_widget.set_marker(location['coordenadas'][0],location['coordenadas']
                    [1],text=location['direccion'],image=plane_image,text_color="white",
                                 marker_color_circle="black", marker_color_outside="red", font=("Bold", 15), image_zoom_visibility=(0, float("inf")))
                    # self.map_widget.add_left_click_map_command(lambda cordenadas:self.openWindows(cordenadas,destino.id))
                    item = location['coordenadas'],location['direccion']
                    self.ScrollableLabelButtonFrame.command = self.view_location
                    self.ScrollableLabelButtonFrame.comandAddPath = self.marker_path
                    self.ScrollableLabelButtonFrame.add_item(destino.nombre,item,destino.id,(location['coordenadas'][0],location['coordenadas'][1]))
            else:
                    self.ScrollableLabelButtonFrame.add_NotFound()
            self.search_entry.delete(0, ctk.END)
    def view_location(self,cordenadas=None,id_ubicacion=None):
        print('Hola mundoo',id_ubicacion)
        # print('mostrandooooo',cordenadas[0][0],cordenadas[0][1])
        self.map_widget.set_position(cordenadas[0][0], cordenadas[0][1])
        self.openWindows(id_ubicacion)
    def openWindows(self,id_ubicacion):
        self.controllerMap.open_windows(self.viewMain,id_ubicacion)
    def marker_path(self,tupla_cordenadas,id_destino):
        confirm = messagebox.askokcancel("Confirmar", "¿Estás de que quieres agregar una ruta a tu lista de visitas?")
        if confirm:
            self.add_path_history(id_destino)
            self.list_path.append(tupla_cordenadas)
            if len(self.list_path) >= 2 :
                self.map_widget.set_path(self.list_path)
            else:
                messagebox.showinfo('recuerda','recuerda para crear un ruta debes agregar mas de una ruta')
    def add_path_history(self,destino_id):
        self.controllerMap.add_path_history_user(destino_id)
         