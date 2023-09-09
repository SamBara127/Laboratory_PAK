print("Введите число: ", end = '')
d = input() 
print("Простые числа: ", end = '')
nat = True
for k in range(1, int(d)):
    for j in range(1, k):
        if ((k % j == 0) and ((j != 1) and (j != k))):
            nat = False
    if nat == True:
        if k != 1:
            print(k, end = " ")
    nat = True
