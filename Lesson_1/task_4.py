print("Введите год: ", end = '')
y = input() 
ch = int(y) % 4
if ch == 0:
    print("Год является високосным")
else:
    print("Год не является високосным")