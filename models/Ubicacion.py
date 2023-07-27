from typing import List
class Ubicacion:
    def __init__(self,id:int,direccion:str,coordenadas:List[float]) -> None:
        self.id = id
        self.direccion = direccion
        self.coordenadas = coordenadas
    # agregar el decorador para convertir en json o el json convertirlo en un objecto
    