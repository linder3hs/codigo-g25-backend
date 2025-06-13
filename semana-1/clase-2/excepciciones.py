print("="*20, "ZeroDivisionError","="*20)
print("="*20, "ValueError","="*20)

def dividir():
  try:
    numero1 = int(input("Ingrese el n1: "))
    numero2 = int(input("Ingrese el n2: "))
    print(numero1 / numero2)
  except ZeroDivisionError:
    print("No es posible dividir entre 0")
  except ValueError as e:
    print(f"Error: {e}")
  except Exception as e:
    print(f"Error: {e}")
  finally:
    print("La operación termino")

  print("="*20, "IndexError","="*20)
  try:
    letras = ['a', 'b', 'c', 'd']
    print(letras[10])
  except IndexError as e:
    print(f"Error: {e}")

dividir()

print("="*20, "Exeption","="*20)
try:
  alumnos = ["pepe", "luis"]
  print(alumnos[5])
except Exception as e:
  print(f"Error: {e}")

try:
  persona = {"id": 1, "name": "Linder"}
  persona["lastname"]
except KeyError as e:
  print(f"Error: El key {e} no se encontro")
