from datetime import datetime

class Actividad:
    def __init__(self,id:int,nombre:str,destino_id:int,hora_inicio:str | datetime):
        self.id = id
        self.nombre = nombre
        self.destino = destino_id
        self.hora_inicio = hora_inicio
    # agregar el decorador para convertir en json o el json convertirlo en un objecto
