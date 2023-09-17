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

if (len(lst[0]) < len(lst2[0]) or len(lst) < len(lst2)):
    print('OPS!!!')
    exit()
print("OK")

buf = 0

with open('output.txt', 'w') as f:
    for i in range(len(lst)-len(lst2)+1):
        for j in range(len(lst[0])-len(lst2[0])+1):
            for x in range(len(lst2)):
                for y in range(len(lst2[0])): 
                    buf += int(lst2[x][y]) * int(lst[x+i][y+j])
            f.write(str(buf) + ' ')
            buf = 0
        f.write('\n')