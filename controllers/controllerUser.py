# from main import Main
from models.Usuario import Usuario
class ControllerUser:
    def __init__(self,app):
        self.app = app
        self.session = None
    def register_user(self):
            data_user = self.app.user_view.return_data_user()
            newUser = Usuario(**data_user)
            comprobate_errors = newUser.comprobate_property()
            if len(comprobate_errors) > 0 :
                 self.app.user_view.meesageError(comprobate_errors)
            else:
                searchUser = newUser.searchUser(newUser.email)
                if not searchUser :
                     newUser.CreateUser()
                     self.app.user_view.messageSuccess()
                else:
                     print("El usuario ya existe")
                     self.app.user_view.meesageError('El usuario ya esta registrado, intente iniciar sesion')
                                   
    def navigate_login(self):
         self.app.change_frame(self.app.user_view_login)