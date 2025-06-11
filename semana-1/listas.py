# arreglo => lista
alumnos = ["Juan", "Irving", "Nicolas", "Lucas", "Mario"]
print(alumnos[3])
# agregar un valor
print("*"*10, 'Append', "*"*10)
alumnos.append("Jefferson")
print(alumnos)
# eliminr un valor
print("*"*10, 'Remove', "*"*10)
alumnos.remove("Lucas")
print(alumnos)
# insert
print("*"*10, 'Insert', "*"*10)
alumnos.insert(3, "Alex")
print(alumnos)
print("*"*10, 'Sort', "*"*10)
alumnos.sort()
print(alumnos)
print("*"*10, 'Reverse', "*"*10)
alumnos.reverse()
print(alumnos)
print("*"*10, 'Len', "*"*10)
print(len(alumnos))
print("*"*10, 'Index', "*"*10)
print(alumnos.index("Juan"))
# print(alumnos.index("Pepe"))
