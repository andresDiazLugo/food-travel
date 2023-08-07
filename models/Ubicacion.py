from typing import List
import os
import json
class Ubicacion:
    def __init__(self,id:(int | None )=None,direccion:(str | None)=None,coordenadas:(List[float] | None)=None) -> None:
        self.id = id
        self.direccion = direccion
        self.coordenadas = coordenadas
    # agregar el decorador para convertir en json o el json convertirlo en un objecto
    def searchUbicacion(self,value):
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory,'data/ubicacion.json')
        if os.path.exists(file_path):
              with open(file_path, 'r') as file:
                data = json.load(file)
                for ubicacion in data['ubicaciones']:
                    if self.searchKey(ubicacion,value):
                         return ubicacion
                return False
                    
    def searchKey(self,dicc,value_comparate):
        for key,value in dicc.items():
              if(value == value_comparate):
                   return True
        return False