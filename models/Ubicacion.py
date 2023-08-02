from typing import List
class Ubicacion:
    def __init__(self,id:int,direccion:str,coordenadas:List[float]) -> None:
        self.id = id
        self.direccion = direccion
        self.coordenadas = coordenadas
    # agregar el decorador para convertir en json o el json convertirlo en un objecto    
ubicacion_1 = Ubicacion(
    id=1,
    direccion="Calle Arzobispo Mayoral, 5, 46002, Valencia, España",
    coordenadas=[39.46940, -0.37819]
)

ubicacion_2 = Ubicacion(
    id=2,
    direccion="Av. Revolución, San Pedro de los Pinos, Benito Juárez, Ciudad de México, México",
    coordenadas=[19.39222, -99.17918]
)

ubicacion_3 = Ubicacion(
    id=3,
    direccion="1-2 Shibuya, Shibuya City, Tokyo 150-0002, Japón",
    coordenadas=[35.65911, 139.70392]
)

ubicacion_4 = Ubicacion(
    id=4,
    direccion="1235 Rue Sainte-Catherine Est, Montréal, QC H2L 2H1, Canadá",
    coordenadas=[45.51540, -73.55914]
)

ubicacion_5 = Ubicacion(
    id=5,
    direccion="Jalan Panglima Polim No.33, RT.1/RW.1, Melawai, Kec. Kby. Baru, Kota Jakarta Selatan, Daerah Khusus Ibukota Jakarta 12160, Indonesia",
    coordenadas=[-6.25169, 106.79994]
)

ubicacion_6 = Ubicacion(
    id=6,
    direccion="Via Margherita di Savoia, 52, 80053 Castellammare di Stabia NA, Italia",
    coordenadas=[40.70389, 14.48899]
)

ubicacion_7 = Ubicacion(
    id=7,
    direccion="Leof. Vasilissis Olgas 1, Thessaloniki 546 40, Grecia",
    coordenadas=[40.62489, 22.95334]
)

ubicacion_8 = Ubicacion(
    id=8,
    direccion="138, E. Masjid Moth, Greater Kailash IV, Greater Kailash, Nueva Delhi, Delhi 110048, India",
    coordenadas=[28.55321, 77.24288]
)
     