print('Введите строку: ', end='')
st = input()
st = st.lower()
l = int(len(st)/2)
res=''.join(reversed(st[-l:]))
if (st[:l] == res): 
    print("Данная строка является палиндромом")
else:
    print("Данная строка не является палиндромом")
# print(st[:l])
# res=''.join(reversed(st[-l:]))
# print(res)
# print(st[-l:])
