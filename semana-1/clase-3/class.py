# clase o entidad
class Auto:
    """-"""
    # abstraccion, definir los atributos que van a permitir crear la clase
    # los atributos sera recibida cundo se instancie (cree) la clase, por ende pora
    # poder recibir los valores, vamos un constructor
    # para crear un constructor en python, tenemos la palabra reserveda __init__
    # una regla de las funciones dentro de una class, es que siempre el primer parametro sea self
    # los parametros es la informacion que recibimos al instaciar la clase y esa informacion
    # debemos guardarla dentro del contructor para poder usarla dentro de otras funciones
    def __init__(self, marca, modelo, placa, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.kilometraje = kilometraje

    def mostrar_informacion(self):
        """-"""
        print(f"Carro: {self.marca} {self.modelo}")

# instancia 1
auto_1 = Auto("Jeep", "Compass", "ABC-123", 34500)
auto_1.mostrar_informacion()
# instancia 2
auto_2 = Auto("Subaru", "XRV", "ZXC-987", 1200)
auto_2.mostrar_informacion()
