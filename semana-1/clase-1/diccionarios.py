# dict => obj
persona = {
  "nombre": "Linder",
  "nombre": "Anderson",
  "edad": 25,
  # "direccion": "av mi casa 123",
  1: "numero"
}
persona["profesion"] = "Programador"
print(type(persona))
print(persona)
# obtener algun valor del dict usamos get
# print(persona["direccion"])
print(persona.get("direccion", "no encontrado"))
print("="*10, "UPDATE", "="*10)
persona.update({"direccion": "av mi casa2"})
print(persona)
persona.pop(1)
print(persona)
print(persona.keys())
print(persona.values())
