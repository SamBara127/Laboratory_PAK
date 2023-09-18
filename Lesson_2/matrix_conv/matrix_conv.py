
def init_matrix(fn):
    lst = []
    lst2 = []
    sel = 0
    ls = []
    st = '1'
    with open(fn, 'r') as f:
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

    if (len(lst[0]) < len(lst2[0]) or len(lst) < len(lst2)):
        print('Данные матрицы нельзя перемножить!!!')
        exit()
    print("Выдана матрица №1 = ", end='')
    print(lst)
    print("Выдана матрица №2 = ", end='')
    print(lst2)

    return lst, lst2

def matrix_conv(fn, lst, lst2):
    buf = 0
    with open(fn, 'w') as f:
        for i in range(len(lst)-len(lst2)+1):
            for j in range(len(lst[0])-len(lst2[0])+1):
                for x in range(len(lst2)):
                    for y in range(len(lst2[0])): 
                        buf += int(lst2[x][y]) * int(lst[x+i][y+j])
                f.write(str(buf) + ' ')
                buf = 0
            f.write('\n')
    print('Файл с матрицей записан!')


if __name__ == "__main__":

    fin = 'input.txt'
    fon = 'output.txt'

    mat_1, mat_2 = init_matrix('input.txt')
    matrix_conv('output.txt', mat_1, mat_2)