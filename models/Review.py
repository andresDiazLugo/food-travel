class Review:
    def __init__(self,id:int,id_destino:int,id_usuario:int,calificacion:int,comentario:str,anonimo:bool):
        self.id = id
        self.id_destino = id_destino
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.anonimo = anonimo