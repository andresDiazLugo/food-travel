from typing_extensions import Literal
from typing import List

#tipando una variable con ocpiones especificas
categoria = Literal['Italiana','Mediterranea','Regional','Hindu']
class Destino_culinario:
    def __init__(self,id:int,nombre:str,tipo_cocina:categoria,ingredientes:List[str],precio_minimo:float,precio_maximo:float,popularidad:float,disponibilidad:bool,id_ubicacion:int,imagen:str):
        self.id = id
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.ingredientes = ingredientes
        self.precio_minimo = precio_minimo
        self.precio_maximo = precio_maximo
        self.popularidad = popularidad
        self.disponibilidad = disponibilidad
        self.id_ubicacion = id_ubicacion
        self.imagen = imagen
    # agregar el decorador para convertir en json o el json convertirlo en un objecto

