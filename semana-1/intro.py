"""
- Variables, Sintaxis, Tipos de Datos
strings: str
numeros enteros: int
numeros decimales: float
boleans: bool
null: None

Lenguaje fuertemente tipado como no
"""

altura = None # null
curso = "Backend" # string -> str
edad = 30 # int
altura = 1.8 # float

# usamos _ (snake_case)
es_estudiante = True # bool
es_mayor = False # bool
nombre_completo = "Linder Hassinger" # str

print(altura)
print(curso)
print(es_estudiante)

"""
Operadores
- Aritméticos => +, -, *, /, **, //, %
- Comparación => ==, !=, >, <, >=, <=
- Lógicos => and, or, not, is
"""

print("="*20, "Operadores Aritméticos", "="*20)
n1 = 10
n2 = 5
print("Suma", n1 + n2)
print("Resta", n1 - n2)
print("Producto", n1 * n2)
print("Division", n1 / n2)
print("Residuo", n1 % n2)
print("Potencia", n1 ** n2)
print("Division", n1 // n2)
# f, string
print("="*20, "Operadores de Comparación", "="*20)
print(f"Igualdad: {n1 == n2}")
print(f"Diferencia: {n1 != n2}")
print(f"Mayor: {n1 > n2}")
print(f"Menor: {n1 < n2}")
print("="*20, "Operadores Lógicos", "="*20)
print(n1 == 10 and n2 == 5)
print(n1 > 10 or n2 <= 5)

if n1 == 10 and n2 <= 5:
  message = "Se encontro alguna coincidencia"
  print(message)
else:
  print("No hay coincidencias")
