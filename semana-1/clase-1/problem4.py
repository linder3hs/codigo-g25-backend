"""
Pedir al usuario 3 notas y evaluar el promedio de estos, en caso el promedio sea mayor a 16
imprimir sobresaliente, caso contrario imprimir en trabajo
"""
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))

promedio = (nota1 + nota2 + nota3) / 3

print(promedio, "Sobresaliente" if promedio > 16 else "En Trabajo")
