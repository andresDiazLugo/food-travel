from typing import List
import os
import json
import re

class Usuario:
    def __init__(self,id:(str | None)=None,email:(str | None)=None,password:(str | None)=None, nombre:(str | None)=None, apellido:(str | None)=None,historial_rutas:(List[int | None])=[]) -> None:
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
    def add_element_history_path(self,sesion,value=None):
        email = sesion['email']
        found_email:Usuario = self.searchUser(email)
        if found_email :
            current_directory = os.getcwd()
            file_path = os.path.join(current_directory,'data/users.json')
            with open(file_path, 'r') as file:
                data = json.load(file)
                user_id = sesion['id']
                user_index = next((index for (index, user) in enumerate(data['usuarios']) if user['id'] == user_id), None)
                if user_index is not None:
                    data['usuarios'][user_index]['historial_rutas'].append(value)
                    with open(file_path, 'w') as json_data:
                        json.dump(data, json_data, indent=4)
                        return True
                else:
                    return False
        else:
            return False
    def delete_all_history_path(self,sesion):
            print('entrandiii')
            current_directory = os.getcwd()
            file_path = os.path.join(current_directory,'data/users.json')
            with open(file_path, 'r') as file:
                data = json.load(file)
                user_id = sesion['id']
                user_index = next((index for (index, user) in enumerate(data['usuarios']) if user['id'] == user_id), None)
                if user_index is not None:
                    data['usuarios'][user_index]['historial_rutas']=[]
                    with open(file_path, 'w') as json_data:
                        json.dump(data, json_data, indent=4)
                        return True
                else:
                    return False
    def delete_history_path(self,sesion,id=None):
            current_directory = os.getcwd()
            file_path = os.path.join(current_directory,'data/users.json')
            with open(file_path, 'r') as file:
                data = json.load(file)
                user_id = sesion['id']
                user_index = next((index for (index, user) in enumerate(data['usuarios']) if user['id'] == user_id), None)
                if user_index is not None:
                    filter_user_id = [element for element in data['usuarios'][user_index]['historial_rutas'] if element != id ]
                    print('filter',filter_user_id, id)
                    data['usuarios'][user_index]['historial_rutas'] = filter_user_id
                    with open(file_path, 'w') as json_data:
                        json.dump(data, json_data, indent=4)
                        return True
                else:
                    return False