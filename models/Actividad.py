from datetime import datetime
class Actividad:
    def __init__(self,id:int,nombre:str,destino_id:int,hora_inicio:str | datetime):
        self.id = id
        self.nombre = nombre
        self.destino = destino_id
        self.hora_inicio = hora_inicio
    # agregar el decorador para convertir en json o el json convertirlo en un objecto
from datetime import datetime



# Crear instancias de Actividad
actividad_1 = Actividad(
    id=1,
    nombre="Elias",
    destino_id=1,  # ID del destino asociado
    hora_inicio=datetime(2023, 5, 15, 10, 0)  # Fecha y hora de inicio
)

actividad_2 = Actividad(
    id=2,
    nombre="Alberto",
    destino_id=2,  # ID del destino asociado
    hora_inicio="2023-05-20 15:30"  # Formato de cadena de fecha y hora
)

actividad_3 = Actividad(
    id=3,
    nombre="Andres",
    destino_id=1,  # ID del destino asociado
    hora_inicio=datetime(2023, 5, 15, 19, 0)  # Fecha y hora de inicio
)

# Mostrar la información de las actividades
actividades = [actividad_1, actividad_2, actividad_3]

for actividad in actividades:
    print(f"Actividad ID: {actividad.id}")
    print(f"Nombre: {actividad.nombre}")
    print(f"Destino ID: {actividad.destino_id}")
    print(f"Hora de Inicio: {actividad.hora_inicio}")
    print("------------------------------")
