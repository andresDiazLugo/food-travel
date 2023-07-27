from typing import List
class Ruta_Visita:
    def __init__(self,id:int,nombre:str,desitnos:List[int]):
        self.id = id
        self.nombre = nombre
        self.destinos = desitnos
    # agregar el decorador para convertir en json o el json convertirlo en un objecto
