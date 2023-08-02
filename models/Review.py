class Review:
    def __init__(self,id:int,id_destino:int,id_usuario:int,calificacion:int,comentario:str,anonimo:bool):
        self.id = id
        self.id_destino = id_destino
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.anonimo = anonimo

class Usuario:
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre

# Crear instancias de usuarios
usuario_1 = Usuario(id=1, nombre="Elias")
usuario_2 = Usuario(id=2, nombre="Alberto")
usuario_3 = Usuario(id=3, nombre="Andres")

# Crear instancias de reseñas
review_1 = Review(
    id=1,
    id_destino=1,  # ID del destino asociado
    id_usuario=1,  # ID del usuario que hace la reseña
    calificacion=4,  # Calificación de la reseña
    comentario="Excelente lugar para probar comida local.",  # Comentario de la reseña
    anonimo=False  # Si es anónimo o no
)

review_2 = Review(
    id=2,
    id_destino=2,  # ID del destino asociado
    id_usuario=2,  # ID del usuario que hace la reseña
    calificacion=5,  # Calificación de la reseña
    comentario="El mejor lugar que he visitado hasta ahora.",  # Comentario de la reseña
    anonimo=False  # Si es anónimo o no
)

review_3 = Review(
    id=3,
    id_destino=1,  # ID del destino asociado
    id_usuario=3,  # ID del usuario que hace la reseña
    calificacion=3,  # Calificación de la reseña
    comentario="La comida no estuvo mal, pero el servicio fue lento.",  # Comentario de la reseña
    anonimo=True  # Si es anónimo o no
)

# Crear una lista de reseñas
reseñas = [review_1, review_2, review_3]

# Mostrar la información de las reseñas
for reseña in reseñas:
    print(f"Reseña ID: {reseña.id}")
    print(f"Destino ID: {reseña.id_destino}")
    print(f"Usuario ID: {reseña.id_usuario}")
    print(f"Calificación: {reseña.calificacion}")
    print(f"Comentario: {reseña.comentario}")
    print(f"Anónimo: {reseña.anonimo}")
    print("------------------------------")
