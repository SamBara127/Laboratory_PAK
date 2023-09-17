import random as rnd


print('Введите число чисел в генерации: ', end='')
st = input()
num = int(st)
lst = [rnd.randint(0, num) for i in range(num)]
print(lst)
chet = 0
n_chet = 0
it =  iter(lst)
for i in it:
    if (i % 2 == 0):
        chet += 1
    else: 
        n_chet += 1
print('Колличество четных чисел - ' + str(chet))
print('Колличество нечетных чисел - ' + str(n_chet))