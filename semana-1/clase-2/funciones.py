# FUNCIONES
def saludar():
  print("Hola, esta es mi primera function")

print("Fuera de la funcion")

saludar()

def sumar(numero1, numero2):
  print(numero1 + numero2)

def elevar_a_la_potencia(numero, potencia):
  return numero ** potencia

def recolectar_informacion():
  while True:
    nombre = input("Ingrese su nombre*: ")
    if nombre != "":
      break
  apellido = input("Ingrese su apellido: ")
  print(type(nombre))
  return f"Hola me llamo {nombre} {apellido}"

sumar(10, 20)

operacion = elevar_a_la_potencia(2, 8)
print("operacion", operacion)

recoleccion = recolectar_informacion()
print(recoleccion)

def dividir(n1, n2) -> float:
  return n1 / n2

print("dividir", dividir(10,3))

def sumatoria(*args):
  return sum(args)

print("sumatoria", sumatoria(1,2,3,5,6,1,1,1))

# FUNCIONES ANONIMAS
duplicar = lambda n1: n1* 2

print("duplicar", duplicar(92))
