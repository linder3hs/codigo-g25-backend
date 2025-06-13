import math
import random
import datetime
import time

print("MATH")
print(math.pi)
print(math.floor(2.8))
print(math.ceil(2.8))
print(math.sqrt(100))
print(math.sqrt(3))
print(math.log10(1000))
print(math.factorial(5))
print(math.pow(2, 3))

print("RANDOM")
print(random.randint(1, 10))
print(random.uniform(0, 2))

participantes = ["Pepe", "Jaun", "Luis"]
print(random.choice(participantes))
random.shuffle(participantes)
print(participantes)

print(datetime.datetime.now())
# print(time.time())
hoy = datetime.date.today()
print(hoy.strftime("%a %m/%y"))
