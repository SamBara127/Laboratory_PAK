

lst = []
lst2 = []
sel = 0
ls = []
st = '1'
with open('input.txt', 'r') as f:
    while(st != ''):
        st = f.readline()
        if st != '\n':
            st = st[:-1]
            ls = st.split(' ')
            if sel == 0:
                lst.append(ls)
            else:
                lst2.append(ls)
        else:
            sel = 1
lst2.pop()
print(lst)
print(lst2)

if len(lst[0]) != len(lst2):
    print('OPS!!!')
    exit()
print("OK")

buf = 0
new_lst = []

with open('output.txt', 'w') as f:
    for i in range(len(lst)):
        for j in range(len(lst2[0])):
            for k in range(len(lst2)):
                buf += int(lst[i][k]) * int(lst2[k][j])
            new_lst.append(buf)
            f.write(str(buf) + ' ')
            buf = 0
        f.write('\n')