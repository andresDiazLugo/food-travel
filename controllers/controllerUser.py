# from main import Main
from models.Usuario import Usuario
class ControllerUser:
     def __init__(self,app):
        self.app = app
        self.session = None
     #    self.session =  {"id": '04d47e15-44ec-44a7-91b2-a4ca87a7fd2c', "nombre": 'Andres', "apellido": 'DIaz', "email": 'myemail1@gmail.com', "password": 'mypassword', "historial_rutas": []}
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
                     self.navigate_login()
                else:
                     self.app.user_view.reset_value_camp()
                     self.app.user_view.meesageError('El usuario ya esta registrado, intente iniciar sesion')
     def signin(self):
          data_user_login = self.app.user_view_login.return_data_user()
          newUserLogin = Usuario(**data_user_login)
          comprobate_errors = newUserLogin.comprobate_property()
          if len(comprobate_errors) > 0:
               self.app.user_view_login.meesageError(comprobate_errors)
          else:
               searchUser = newUserLogin.searchUser(newUserLogin.email)
               if searchUser:
                    if searchUser['password'] == newUserLogin.password:
                         self.session = searchUser
                         self.navigate_home()
                         self.app.home_view.name_user.configure(text=self.session['nombre'])
                         print('esta es la session',self.session)
                    else:
                         self.app.user_view_login.meesageError('El email o password son incorrectos, vuelve a intentar')
               else:
                    self.app.user_view_login.meesageError('El usuario no esta registrado en nuestro sistema,registrate')
     def navigate_login(self):
         self.app.change_frame(self.app.user_view_login)
     def navigate_register(self):
         self.app.change_frame(self.app.user_view)
     def navigate_home(self):
          self.app.change_frame(self.app.home_view)