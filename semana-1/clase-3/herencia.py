"""
Persona
- nombre
- fecha_nacimiento
- dni
- nacionalidad

Estudiante
- nombre
- fecha_nacimiento
- dni
- nacionalidad
- codigo
- correo_estudiantil

Empleado
- nombre
- fecha_nacimiento
- dni
- nacionalidad
- codigo_empleado
- correo_corporativo
- salario

atributos privados: son atributos en el cual su valor solo puede ser accecido desde
la misma clase, es decir la instancia no puede acceder
la forma en la que indicamos que un atributo es privado es colocando el __ delante del nombre
"""

class Persona:
    """Function printing python version."""


    def __init__(self, nombre, fecha_nacimiento, dni, nacionalidad):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.dni = dni
        self.nacionalidad = nacionalidad


    def saludar(self):
        """Function printing python version."""
        print(f"Hola me llamo {self.nombre}, naci en {self.fecha_nacimiento}")
        print(f"DNI: {self.dni}")
        print(f"Nacionalidad: {self.nacionalidad}")


# Heredar de Persona
class Estudiante(Persona):
    """-"""


    def __init__(self, nombre, fecha_nacimiento, dni, nacionalidad, codigo, correo_estudiantil):
        # En el contructor de la clase Hija, vamos a volver a pedir los atributos
        # para poder enviarlo a la clase padre, la forma en la que enviamos
        # los atributos es mediante super()
        super().__init__(nombre, fecha_nacimiento, dni, nacionalidad)
        # __ privado
        self.__codigo = codigo
        # _ protegido
        self._correo_estudiantil = correo_estudiantil

    def mostrar_notas(self):
        """print information"""
        print(f"Notas del alumno: {self.nombre}")
        print(f"Codigo: {self.__codigo}")
        print("Nota1: 18")


class Profesor(Persona):
    """Clase Profesor"""


    def __init__(self, nombre, fecha_nacimiento, dni, nacionalidad, asignatura):
        super().__init__(nombre, fecha_nacimiento, dni, nacionalidad)
        self.asignatura = asignatura

    def ensenar(self):
        """Print message"""
        print(f"Profesor {self.nombre} enseña {self.asignatura}")


estudiante_1 = Estudiante("Pepe", "2000-10-01", "888888", "Peruano", "123456", "pepe@gmail.com")
# print("__codigo", estudiante_1.__codigo)
estudiante_1.saludar()
estudiante_1.mostrar_notas()
print("---PROFESOR----")
profesor_1 = Profesor("Juan", "1990-01-01", "01234567", "Español", "Bases de Datos")
profesor_1.ensenar()
