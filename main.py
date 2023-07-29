# importaciones de modulos de terceros
import customtkinter as ctk
# importaciones de controllers
from controllers.controllerUser import ControllerUser
# importaciones de vistas
from views.registerUser import RegisterUser
from views.signinUser import SignInUser
from views.home import Home
class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.s='hola mundoo'
        self.title('Food Travel')
        self.resizable(False,False)
        window_width, window_height = 1000, 700
        self.window_center(window_width,window_height)
        self.initControllerAndViews()
    def window_center(self, w, h):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (w // 2)
        y = (screen_height // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")
    def adjust_frame(self,frame,row=0, column=0,sticky="nsew"):
        frame.grid(row=row,column=column,sticky=sticky)

    def initControllerAndViews(self):
        # instanciamos los controllers
        user_controller = ControllerUser(self)
        # instanciamos las vistas
        self.home_view = Home(self)
        self.user_view_login = SignInUser(self,user_controller)
        self.user_view = RegisterUser(self,user_controller)
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