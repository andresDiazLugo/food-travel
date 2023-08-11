import json

class FavoritosManager:
    def cargar_usuarios(self):
        try:
            with open('data/users.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def guardar_usuarios(self, usuarios):
        with open('data/users.json', 'w') as f:
            json.dump(usuarios, f, indent=4)

    def agregar_favorito(self, usuario_id, restaurante):
        usuarios = self.cargar_usuarios()

        for usuario in usuarios['usuarios']:
            if usuario['id'] == usuario_id:
                usuario['favoritos'].append(restaurante)
                break

        self.guardar_usuarios(usuarios)

    def quitar_favorito(self, usuario_id, restaurante):
        usuarios = self.cargar_usuarios()

        for usuario in usuarios['usuarios']:
            if usuario['id'] == usuario_id:
                if restaurante in usuario['favoritos']:
                    usuario['favoritos'].remove(restaurante)
                break
