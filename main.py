# importaciones de modulos de terceros
import customtkinter as tk
# importaciones de controllers
from controllers.controllerUser import ControllerUser
# importaciones de vistas
from views.registerUser import RegisterUser
class Main(tk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Food Travel')
        self.resizable(False,False)
        window_width, window_height = 1200, 900
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
    def expand_frame(self,frame):
        frame.pack(expand=True)
    def initControllerAndViews(self):
        # instanciamos los controllers
        user_controller = ControllerUser(self)
        # instanciamos las vistas
        self.user_view = RegisterUser(self,user_controller)
        # configuramos tamañlos o posisiones
        self.expand_frame(self.user_view) 
if __name__ == '__main__':
    app = Main()
    app.mainloop()