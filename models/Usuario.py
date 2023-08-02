from typing import List
import os
import json
import re

class Usuario:
    def __init__(self,id:str,email:str,password:str, nombre:str, apellido:str,historial_rutas:(List[int | None])=[]) -> None:
        self.id = id
        self.email = email
        self.password = password        
        self.nombre = nombre
        self.apellido = apellido
        self.historial_rutas = historial_rutas
    # agregar el decorador para convertir en json o el json convertirlo en un objecto
    def CreateUser(self):
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory,'data/users.json')
        if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    data_user = {
                         'id' : self.id,
                         'nombre' : self.nombre,
                         'apellido' : self.apellido,
                         'email' : self.email,
                         'password' : self.password,
                         'historial_rutas': self.historial_rutas
                    }
                    data['usuarios'].append(data_user)
                    print('ess',data_user)
                    with open(file_path,'w') as file:
                         json.dump(data,file,indent=4)
                         print("El usuario se registro con exito")

    def searchUser(self,value):
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory,'data/users.json')
        if os.path.exists(file_path):
              with open(file_path, 'r') as file:
                data = json.load(file)
                for user in data['usuarios']:
                    self.searchKey(user,value)
                    if self.searchKey(user,value):
                         return user
                return False
              
    def searchKey(self,dicc,value_comparate):
        for key,value in dicc.items():
              if(value == value_comparate):
                   return True
        return False
    def comprobate_property(self):
        def es_email_valido(email):
            # Expresión regular para validar emails
            patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            return re.match(patron, email) is not None
        errors = []
        if self.nombre == '':
              errors.append('El nombre es obligatorio')
        if self.apellido == '':
             errors.append('El apellido es obligatorio')
        if self.email == '':
            errors.append('El email es obligatorio')
        if self.password == '':
            errors.append('El password es obligatorio')
        if not es_email_valido(self.email):
            errors.append('El email tiene que ser un email valido')
        if len(errors) > 0 :
             errors = ",".join(errors)
             return errors
        else:
             return errors
    