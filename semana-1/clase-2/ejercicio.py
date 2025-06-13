def calcular_total(productos):
  sub_total = 0
  for producto in productos:
    sub_total += producto.get("precio")

  total = sub_total * 1.18
  descuento = 0
  if total >= 500:
    descuento = 10
    total -= descuento

  return {
    "sub_total": sub_total,
    "total": total,
    "descuento": descuento
  }

def recolectar_informacion():
  try:
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")

    productos = []

    for i in range(3):
      nombre_producto = input(f"Ingrese el nombre del producto {i+1}: ")
      precio = float(input("Ingrese el precio del produto: "))

      productos.append({"producto": nombre_producto, "precio": precio})

    datos_boleta = calcular_total(productos)

    print("------- Mi Tiendita ---------")
    print(f"Cliente: {nombre}")
    print(f"Edad: {edad}")

    print("---- Productos -----")
    for producto in productos:
      print(f"{producto.get("producto")} ----------- {producto.get("precio")}")

    print(f"Sub total: {datos_boleta.get("sub_total")}")
    print(f"Descuento: {datos_boleta.get("descuento")}")
    print(f"Total: {datos_boleta.get("total")}")
  except TypeError as e:
    print(f"TypeError: {e}")
  except Exception as e:
    print(f"Error: {e}")

recolectar_informacion()
