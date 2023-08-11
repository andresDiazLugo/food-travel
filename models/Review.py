import os
import json
import re
class Review:
    def __init__(self,id:(int | None) =None,id_destino:(int | None) = None,id_usuario:(int | None) = None,calificacion:(int | None) = None,comentario:(str | None ) = None,anonimo:(bool | None) = None):
        self.id = id
        self.id_destino = id_destino
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.anonimo = anonimo
    def CreateReview(self):
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory,'data/review.json')
        if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    data_review = {
                         'id' : self.id,
                         'id_destino' : self.id_destino,
                         'id_usuario' : self.id_usuario,
                         'calificacion' : self.calificacion,
                         'comentario' : self.comentario,
                         'anonimo': self.anonimo
                    }
                    data['reviews'].append(data_review)
                    with open(file_path,'w') as file:
                         json.dump(data,file,indent=4)
                         return True
        else:
             return False
    def find_all(self):
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory,'data/review.json')
        if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    return data['reviews']
        else:
             return False