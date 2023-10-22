import numpy as np

with open('file_1.txt', 'r') as f:
    st = f.readline()
    ls = st.split(' ')
    ls = [int (x) for x in ls]
    arr_1 = np.array(ls)

with open('file_2.txt', 'r') as f:
    st = f.readline()
    ls = st.split(' ')
    ls = [int (x) for x in ls]
    arr_2 = np.array(ls)


if __name__ == "__main__":
    print("Введите вероятность: ", end='')
    p = input()
    p_real = round(float(p) * len(arr_1))
    emp = np.empty(p_real)
    uni = 0
    while(uni == 0):
        uni = 1
        for i in range(p_real):
            emp[i] = np.random.randint(len(arr_1))
        for i in range(p_real):
            for j in range(i+1,p_real):
                if emp[i]==emp[j]:
                    uni = 0
    for i in range(p_real):
        arr_1[int(emp[i])] = arr_2[int(emp[i])]
    print("Результат: ", end='')
    print(arr_1)
    
