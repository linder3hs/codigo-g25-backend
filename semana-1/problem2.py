# Culcular si la edad ingresa por el usuario es mayor o menor
edad = int(input("Ingrese la edad: "))
# para estos casos existe el operador ternario
# else if => elif
resultado = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(resultado)
# if edad >= 18:
#   print("Es mayor edad")
# else:
#   print("Es menor edad")
