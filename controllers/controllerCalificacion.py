from models.Review import Review
from models.Usuario import Usuario
from models.Destino_culinario import Destino_culinario
class Controller_calificacion:
    def __init__(self,app) -> None:
        self.app = app
    
    def save_calificacion(self,data_review):
        # vamos a intanciar la clase Review asi podemos guardar los datos dentro del json y simular una entidad o una coleccion de datos
        review_destion = Review(**data_review)
        confirm_creation = review_destion.CreateReview()
        return confirm_creation
    def return_all_reviews(self):
        return Review().find_all()
    def return_name_user(self,id):
        name_user = Usuario().searchUser(id)
        return name_user['nombre']
    def return_name_destino(self,id):
        name_destino = Destino_culinario().searchDestino(id)
        return name_destino['nombre']