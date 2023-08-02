class Controller_Map:
    def __init__(self,app) -> None:
        self.app = app
        self.list_destinos = []
        self.nombre = ''
        self.cocina_typo = ''
    def precio_menor(self):
        precio = sorted(self.list_destinos,key=lambda x: x.precio_minimo)
        return precio
        
    def precio_mayor(self):
        precio = sorted(self.list_destinos,key=lambda x: x.precio_minimo,reverse=True)
        return precio
    def type_food(self,element):
        if element.tipo_cocina == self.cocina_typo:
            return element
    def search_input(self,element):
        if element.nombre == self.nombre:
            return element
    def add_list(self,newList):
        if len(self.app.destinos_culinarios) > 0:
            self.list_destinos = newList
            return self.list_destinos
    def filterDestinos(self,price=None,searchName=None,type_cocina=None):
            if price == 'precio mayor':
                self.list_destinos = self.precio_mayor()
            if price == 'precio menor':
                self.list_destinos = self.precio_menor()
            if searchName != None and searchName != '' :
                self.nombre = searchName
                self.list_destinos = list(filter(self.search_input,self.list_destinos))
            if type_cocina != None and type_cocina != '':
                self.cocina_typo = type_cocina
                if self.cocina_typo != 'Todos':
                    self.list_destinos = list(filter(self.type_food,self.list_destinos))
            return self.list_destinos
    def search_id_ubicacion(self):
        pass
        