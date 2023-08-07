# importaciones de modulos de terceros
import customtkinter as ctk
# importaciones de modelos
from models.Destino_culinario import Destino_culinario
# importaciones de controllers
from controllers.controllerUser import ControllerUser
from controllers.controllerMap import Controller_Map
# importaciones de vistas
from views.registerUser import RegisterUser
from views.signinUser import SignInUser
from views.navOptions import Nav_Options
from views.map import Map
from views.detailDestino import DetailDestino
class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.s='hola mundoo'
        self.title('Food Travel')
        self.resizable(False,False)
        window_width, window_height = 1000, 700
        self.window_center(window_width,window_height)
        self.get_data_models()
        self.initControllerAndViews()
    def window_center(self, w, h):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (w // 2)
        y = (screen_height // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")
    def adjust_frame(self,frame,row=0, column=0,sticky="nsew"):
        frame.grid(row=row,column=column,sticky=sticky)
    def get_data_models(self):
        self.destinos_culinarios = Destino_culinario.cargar_de_json()
        print('estos son los destinos culinarios',type(self.destinos_culinarios[0]))
    def initControllerAndViews(self):
        # instanciamos los controllers
        user_controller = ControllerUser(self)
        map_controller = Controller_Map(self)
        # instanciamos las vistas
        self.detailview = DetailDestino
        self.map_view = Map
        self.user_view_login = SignInUser(self,user_controller)
        self.user_view = RegisterUser(self,user_controller)
        self.home_view = Nav_Options(self,user_controller,map_controller)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # configuramos tamañlos o posisiones
        self.adjust_frame(self.home_view,0,0)#3tercera pantalla de renderizado
        self.adjust_frame(self.user_view_login,0,0)#2segunda pantalla de renderizado
        self.adjust_frame(self.user_view,0,0)#1primera pantalla de renderizado
    def change_frame(self, frame_address):
        frame_address.tkraise()
if __name__ == '__main__':
    app = Main()
    app.mainloop()