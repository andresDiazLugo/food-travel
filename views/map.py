import customtkinter as ctk
import tkintermapview as tkmap
import tkinter
from controllers.controllerMap import Controller_Map
from views.listofubicaciones import ScrollableLabelButtonFrame

class Map(ctk.CTkFrame):
    def __init__(self,app,list_destinos_culinarios=[],controllermap:Controller_Map | None = None):
        super().__init__(app,width=820,fg_color='orange',height=700)
        self.app = app
        self.controllerMap = controllermap
        self.list_destinos_culinarios = list_destinos_culinarios
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
        
        self.dorpdown_options = ctk.CTkOptionMenu(self.frame_header,values=["Todos","Regional", "Hindu", "Mediterranea"],fg_color='orange')
        self.dorpdown_options.place(x=30,y=120)
        
        
        #listbox para mostrar los destinos
        self.ScrollableLabelButtonFrame = ScrollableLabelButtonFrame(self.frame_header,width=440, fg_color='orange')
        self.ScrollableLabelButtonFrame.place(x=359,y=0)

        self.add_element_scrollLaber()
        
        
        # aca colocaremos el frame que contendra el mapa
        self.frame_map =ctk.CTkFrame(self,width=820,height=490,fg_color='blue')
        self.frame_map.pack(side=ctk.TOP)
        #aca colocaremos el widget mapa
        self.map_widget = tkmap.TkinterMapView(self.frame_map,width=820,height=490,corner_radius=0)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22) 
    def add_element_scrollLaber(self):
            self.controllerMap.add_list(self.list_destinos_culinarios)
            precio = self.state_check_precio.get()
            input_entry = self.search_entry.get()
            type_food = self.dorpdown_options.get()
            print('este es el precio',self.state_check_precio.get())
            print('este es el input',self.search_entry.get())
            print('este es la categoria',self.dorpdown_options.get())
            lista_u = self.controllerMap.filterDestinos(precio,input_entry,type_food)
            self.ScrollableLabelButtonFrame.remove_item()
            if len(lista_u) > 0 :
                print(len(lista_u))
                for destino in lista_u:
                    self.ScrollableLabelButtonFrame.add_item(destino.nombre,print(''))
            else:
                    self.ScrollableLabelButtonFrame.add_NotFound()
            self.search_entry.delete(0, ctk.END)
                 
            # print('esta es la lista',lista_Ubicaciones)
        
        # marker_1 = self.map_widget.set_address("Manuel Castilla, A4401 San Lorenzo, Salta",marker=True)
        # marker_1.set_position(-24.746534, -65.485166)
        # marker_2 = self.map_widget.set_address("salta",marker=True)
        # marker_2.set_position(-24.815813, -65.429430)
        # m = self.map_widget.set_address('coliseo romano',marker=True)
        # m.set_position(41.890353933848374, 12.492177253134408)
        # address = tkmap.convert_address_to_coordinates("Salta san lorenzo")
        # print('mostrar localizacion',address)
        # self.map_widget.set_address('Salta san lorenzo')
        # self.map_widget.set_position(address[0],address[1])

        # address = tkmap.convert_address_to_coordinates("London")
        # self.map_widget.set_position(address)
        # marker_3 = self.map_widget.set_address("salta, san lorenzo",marker=True)
        # marker_3.set_position(-24.817065, -65.414412)
        # self.map_widget.set_position(-24.778919, -65.415182)  #coordenadas
        # marker_2 = self.map_widget.set_address("salta",marker=True)
        # marker_2.set_text('comidas salta')
        #direccion
        # print(marker_1.position, marker_1.text)
        # marker_1.set_text("Colosseo in Rome")con esta funcion seteo la nueva direccion
        # marker_1.set_position(48.860381, 2.338594)  # change position
        # marker_1.delete()