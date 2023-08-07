from typing_extensions import Literal
from typing import List
import os
import json
import re
#tipando una variable con ocpiones especificas
categoria = Literal['Italiana','Mediterranea','Regional','Hindu']
class Destino_culinario:
    def __init__(self,id:(int | None)=None,nombre:(str | None)=None,tipo_cocina:(categoria | None)=None,ingredientes:(List[str] | None)=None,precio_minimo:(float | None)=None,precio_maximo:(float | None)=None,popularidad:(float | None)=None,disponibilidad:(bool | None)=None,id_ubicacion:(int | None)=None,imagen:(str | None)=None):
        self.id = id
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.ingredientes = ingredientes
        self.precio_minimo = precio_minimo
        self.precio_maximo = precio_maximo
        self.popularidad = popularidad
        self.disponibilidad = disponibilidad
        self.id_ubicacion = id_ubicacion
        self.imagen = imagen
    # agregar el decorador para convertir en json o el json convertirlo en un objecto
    @classmethod
    def cargar_de_json(cls):
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory,'data/destion_culinario.json')
        if os.path.exists(file_path):
            with open(file_path, "r") as desinos:
                data = json.load(desinos)
            return [cls(**element) for element in data['destinos_culinarios']]
        else: 
            return False
    def searchDestino(self,value):
        print('entrando al metodo', value)
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory,'data/destion_culinario.json')
        if os.path.exists(file_path):
              with open(file_path, 'r') as file:
                data = json.load(file)
                for destino in data['destinos_culinarios']:
                    self.searchKey(destino,value)
                    if self.searchKey(destino,value):
                         return destino
                return False
    def searchKey(self,dicc,value_comparate):
        for key,value in dicc.items():
              if(value == value_comparate):
                   return True
        return False
        
# class ComidaRegional:
#     def __init__(self, id, nombre, tipo_cocina, ingredientes, precio_minimo, precio_maximo,
#                  popularidad, disponibilidad, id_ubicacion, imagen):
#         self.id = id
#         self.nombre = nombre
#         self.tipo_cocina = tipo_cocina
#         self.ingredientes = ingredientes
#         self.precio_minimo = precio_minimo
#         self.precio_maximo = precio_maximo
#         self.popularidad = popularidad
#         self.disponibilidad = disponibilidad
#         self.id_ubicacion = id_ubicacion
#         self.imagen = imagen
        # por que hay dos dejandolo como original para que se vea la modificacion 

# Crear instancias de ComidaRegional para cada variedad de comida

# Paella Valenciana
# paella_valenciana = ComidaRegional(
#     id=1,
#     nombre="Paella Valenciana",
#     tipo_cocina="Mediterránea",
#     ingredientes="Arroz, pollo, conejo, judías verdes, garrofó, pimiento rojo, tomate, azafrán, aceite de oliva",
#     precio_minimo=15,
#     precio_maximo=30,
#     popularidad="Alta",
#     disponibilidad="Todo el año",
#     id_ubicacion=1,
#     imagen="imagen_paella_valenciana.jpg"
# )

# # Chiles en Nogada
# chiles_en_nogada = ComidaRegional(
#     id=2,
#     nombre="Chiles en Nogada",
#     tipo_cocina="Mexicana",
#     ingredientes="Chiles poblanos, carne de cerdo y res, frutas como manzana, pera y durazno, nueces, crema y granada",
#     precio_minimo=10,
#     precio_maximo=20,
#     popularidad="Alta",
#     disponibilidad="Temporada de agosto a septiembre",
#     id_ubicacion=2,
#     imagen="imagen_chiles_en_nogada.jpg"
# )

# # Sushi
# sushi = ComidaRegional(
#     id=3,
#     nombre="Sushi",
#     tipo_cocina="Japonesa",
#     ingredientes="Arroz, pescado fresco, alga nori, aguacate, pepino, jengibre, wasabi",
#     precio_minimo=8,
#     precio_maximo=25,
#     popularidad="Alta",
#     disponibilidad="Todo el año",
#     id_ubicacion=3,
#     imagen="imagen_sushi.jpg"
# )

# # Poutine
# poutine = ComidaRegional(
#     id=4,
#     nombre="Poutine",
#     tipo_cocina="Canadiense",
#     ingredientes="Papas fritas, queso cheddar en trozos, gravy",
#     precio_minimo=5,
#     precio_maximo=12,
#     popularidad="Moderada",
#     disponibilidad="Todo el año",
#     id_ubicacion=4,
#     imagen="imagen_poutine.jpg"
# )

# # Rendang
# rendang = ComidaRegional(
#     id=5,
#     nombre="Rendang",
#     tipo_cocina="Indonesa",
#     ingredientes="Carne de res, leche de coco, especias, hierbas",
#     precio_minimo=10,
#     precio_maximo=18,
#     popularidad="Moderada",
#     disponibilidad="En restaurantes indonesios",
#     id_ubicacion=5,
#     imagen="imagen_rendang.jpg"
# )

# # Comida Italiana
# comida_italiana = ComidaRegional(
#     id=6,
#     nombre="Pizza Margherita",
#     tipo_cocina="Italiana",
#     ingredientes="Masa de pizza, tomate, mozzarella, albahaca, aceite de oliva",
#     precio_minimo=12,
#     precio_maximo=25,
#     popularidad="Alta",
#     disponibilidad="Todo el año",
#     id_ubicacion=6,
#     imagen="imagen_pizza_margherita.jpg"
# )

# # Comida Mediterránea
# comida_mediterranea = ComidaRegional(
#     id=7,
#     nombre="Ensalada Griega",
#     tipo_cocina="Mediterránea",
#     ingredientes="Lechuga, tomate, pepino, cebolla roja, aceitunas, queso feta, aceite de oliva, orégano",
#     precio_minimo=8,
#     precio_maximo=15,
#     popularidad="Moderada",
#     disponibilidad="Todo el año",
#     id_ubicacion=7,
#     imagen="imagen_ensalada_griega.jpg"
# )

# # Comida Hindú
# comida_hindu = ComidaRegional(
#     id=8,
#     nombre="Curry de Pollo",
#     tipo_cocina="Hindú",
#     ingredientes="Pollo, cebolla, tomate, jengibre, ajo, especias como cúrcuma, comino y cilantro",
#     precio_minimo=10,
#     precio_maximo=20,
#     popularidad="Moderada",
#     disponibilidad="Todo el año",
#     id_ubicacion=8
# )
    # agregar el decorador para convertir en json o el json convertirlo en un objecto

       