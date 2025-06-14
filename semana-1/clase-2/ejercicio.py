import random
import datetime
from tabulate import tabulate

def sumar_sub_total(productos):
  sub_total = 0
  for producto in productos:
    sub_total += producto.get("precio")

  return sub_total

def calcular_total_e_impuesto(sub_total, descuento):
  new_sub_total = sub_total - descuento
  total = new_sub_total * 1.18
  igv = total - new_sub_total
  return {
    "total": total,
    "igv": igv
  }

def calcular_descuento(sub_total):
  # si el sub_total >= 500 descuento 10%
  descuento = 0
  if sub_total >= 500:
    descuento = sub_total * 0.1
  return descuento

def obtener_informacion_para_boleta(productos):
  sub_total = sumar_sub_total(productos)
  descuento = calcular_descuento(sub_total)
  calculo_total_e_impuesto = calcular_total_e_impuesto(sub_total, descuento)
  total = calculo_total_e_impuesto.get("total")
  igv = calculo_total_e_impuesto.get("igv")

  return {
    "sub_total": sub_total,
    "total": total,
    "descuento": descuento,
    "igv": igv
  }

def imprimir_boleta(nombre, edad, productos):
  informacion_boleta = obtener_informacion_para_boleta(productos)
  print("-"*50)
  print("------- MI TIENDITA S.A.C. ---------")
  print("------- RUC: 2011223344551 ---------")
  print("------- Av. Siempre viva 123 -------")
  print("BOLETA DE VENTA ELECTRONICA")
  print(f"Nro B0001-{random.randint(100000, 999999)}")
  print(f"FECHA: {datetime.datetime.now().strftime("%d/%M/%Y %H:%M:%S")}")
  print(f"Cliente: {nombre.upper()}")
  print(f"Edad: {edad} años")

  print("---- Productos -----")
  print(tabulate(productos, headers={'producto': 'Producto', 'precio': 'Precio'}))

  print(f"SUB TOTAL: {informacion_boleta.get("sub_total")}")
  print(f"DESCUENTO: {informacion_boleta.get("descuento")}")
  print(f"I.G.V: : {informacion_boleta.get("igv")}")
  print(f"TOTAL: {informacion_boleta.get("total")}")


def recolectar_informacion():
  try:
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")

    productos = []

    for i in range(3):
      nombre_producto = input(f"Ingrese el nombre del producto {i+1}: ")
      precio = float(input("Ingrese el precio del produto: "))

      productos.append({"producto": nombre_producto, "precio": precio})

    imprimir_boleta(nombre, edad, productos)
  except TypeError as e:
    print(f"TypeError: {e}")
  except Exception as e:
    print(f"Error: {e}")

recolectar_informacion()
