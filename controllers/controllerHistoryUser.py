from models.Usuario import Usuario 
from models.Destino_culinario import Destino_culinario
class Controller_user_history:
    def __init__(self,app):
        self.app = app
    def found_property_history_path(self):
       email_user = self.app.user_controller.session['email']
       found_user = Usuario().searchUser(email_user)
       if found_user:
           return found_user['historial_rutas']
       else:
           return False
    def return_all_history_path(self):
        history_path = self.found_property_history_path()
        list_history = []
        if history_path is not False and len(history_path) > 0:
            for element in history_path:
                destino_culinario = Destino_culinario().searchDestino(element)
                list_history.append(destino_culinario)
            return list_history
        else:
            return False
    def delete_all_history(self):
        session_user = self.app.user_controller.session
        delete_all_confirm = Usuario().delete_all_history_path(session_user)
        return delete_all_confirm
    def delete_user_history_id(self,id):
        session_user = self.app.user_controller.session
        delete_history_user_one_confirm = Usuario().delete_history_path(session_user,id)
        return delete_history_user_one_confirm
    
