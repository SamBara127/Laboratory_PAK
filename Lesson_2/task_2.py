print('Введите строку: ', end='')
st = input()
lst = st.split(' ')
it = iter(lst)
# print(it)
max_it = 0x0
max_d = 0
for i in it:
    if (len(i) > max_d):
        max_d = len(i)
        max_it = i
print(max_it)
    
