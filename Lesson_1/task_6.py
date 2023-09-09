print("Введите число вклада: ", end = '')
x = input() 
print("Введите число годов: ", end = '')
y = input() 
total = int(x)
for i in range(int(y)):
    total = total + (total * 0.1)
print("Сумма вклада = ", str(total))