# for - while
cursos = ["JavaScript", "Python","HTML", "CSS"]

alumnos = [
  { "id": 1, "name": "Alex" },
  { "id": 2, "name": "Jefferson" },
  { "id": 3, "name": "Gustavo"}
]
print(f"Cantidad: {len(alumnos)}")

for curso in cursos:
  print(curso)

for alumno in alumnos:
  print(alumno.get("name"), alumno.get("lastname"))

persona = { "nombre": "Linder", "apellido": "Hassinger", "direccion": "av mi casa 123" }
print("="*20)
for p in persona:
  print(p)
print("="*20)
for i in persona.values():
  print(i)

for j in persona.items():
  key, value = j # ("nombre", "Linder")
  print("destructuracion",key, value)


c1, c2 = ("carro1", "carro2")
print(c1, c2)

print("="*20, "WHILE", "="*20)

while True:
  dato = input("Ingrese un valor: ")
  print(dato)
  if dato == "test":
    break # terminar la ejecucion del bucle

contador = 0

while contador <= 5:
  print(contador)
  contador += 1
