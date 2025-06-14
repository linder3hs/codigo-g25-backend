import math
"""
ControlRemoto

TVLG
TVSamsung
TVSonny

Animal
- raza
- nro_patas
- nombre
- fecha_nacimiento

def sonido():
  print("Sonido")

Perro(Animal)

Gato(Animal)
"""

class Animal:
    """ Animal class """

    def sonido(self):
        """NotImplementedError"""
        raise NotImplementedError


class Perro(Animal):
    """ Perro Class """

    def sonido(self):
        print("Gauuu!")


class Gato(Animal):
    """ Gatos Class """

    def sonido(self):
        print("Miauuu!")

perro = Perro()
gato = Gato()

perro.sonido()
gato.sonido()


class Figura:
    """-"""
    def area(self):
        """-"""
        raise NotImplementedError


class Circulo(Figura):
    """-"""
    def __init__(self, radio):
        super().__init__()
        self.radio = radio

    def area(self):
        print(math.pi * math.pow(self.radio, 2))


class Rectangulo(Figura):
    """-"""
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def area(self):
        """-"""
        print(self.base * self.altura)
