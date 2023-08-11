# importaciones de modulos de terceros
import customtkinter as ctk
# importaciones de modelos
from models.Destino_culinario import Destino_culinario
# importaciones de controllers
from controllers.controllerUser import ControllerUser
from controllers.controllerMap import Controller_Map
from controllers.controllerHistoryUser import Controller_user_history
from controllers.controllerCalificacion import Controller_calificacion
# importaciones de vistas
from views.registerUser import RegisterUser
from views.signinUser import SignInUser
from views.navOptions import Nav_Options
from views.map import Map
from views.detailDestino import DetailDestino
from views.userHistory import UserHistory
from views.calificacion import Calificacion
from views.reviews import Reviews
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
        self.user_controller = ControllerUser(self)
        map_controller = Controller_Map(self)
        self.history_user_controller = Controller_user_history(self)
        self.calificacion_controller = Controller_calificacion(self)
        
        # instanciamos las vistas
        self.reviews_views = Reviews
        self.calificacion_view = Calificacion
        self.history_user_view = UserHistory
        self.detailview = DetailDestino
        self.map_view = Map
        self.home_view = Nav_Options(self,self.user_controller,map_controller)
        self.user_view_login = SignInUser(self,self.user_controller)
        self.user_view = RegisterUser(self,self.user_controller)
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