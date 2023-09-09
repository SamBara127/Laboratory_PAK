import math


print("Введите радиус: ", end = "")
r = input()
s = 4 * math.pi * (int(r) ** 2) 
v = (4 / 3) * math.pi * (int(r) ** 3)
print("Площадь сферы = " + str(s))
print("Объем шара = " + str(v))