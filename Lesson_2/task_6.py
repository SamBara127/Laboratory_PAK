
st = '1'
ks, kv, kb = 0, 0, 0
with open('test.txt', 'r') as f:
    while(st != ''):
        st = f.readline()
        ks += 1
        st = st[:-1] # due to delete '\n'
        lst = st.split(' ')
        kv += len(lst)
        it = iter(lst)
        for i in it:
            for j in range(len(i)):
                if i[j].isalpha() == True:
                    kb += 1
print('Колличество строк = ' + str(ks-1))
print('Колличество слов = ' + str(kv-1))
print('Колличество букв = ' + str(kb))
