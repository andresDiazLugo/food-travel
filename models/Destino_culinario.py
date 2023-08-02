from typing_extensions import Literal
from typing import List
import os
import json
import re
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
    @classmethod
    def cargar_de_json(cls):
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory,'data/destion_culinario.json')
        if os.path.exists(file_path):
            with open(file_path, "r") as desinos:
                data = json.load(desinos)
            return [cls(**element) for element in data['destinos_culinarios']]
        else: 
            return False