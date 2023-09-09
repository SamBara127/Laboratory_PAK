import random


buf = 0
k = random.randint(1, 100000)
print("RANDOM VALUE = " + str(k))
while(k != 0):
    buf += k % 10
    k //= 10
print("SUM VALUE = " + str(buf))