from typing import List
class Usuario:
    def __init__(self,id:int,email:str,password:str, nombre:str, apellido:str,historial_rutas:List[int]) -> None:
        self.id = id
        self.email = email
        self.password = password        
        self.nombre = nombre
        self.apellido = apellido
        self.historial_rutas = historial_rutas
    # agregar el decorador para convertir en json o el json convertirlo en un objecto
