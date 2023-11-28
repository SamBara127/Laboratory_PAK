import argparse as arg
import numpy as np


def init_array(fl_name):
    with open(fl_name, 'r') as f:
        st = f.readline()
        ls = st.split(' ')
        ls = [int (x) for x in ls]
        return np.array(ls)


if __name__ == "__main__":

    parser = arg.ArgumentParser()
    parser.add_argument('value', help='Value of data vector', type=float)
    args = parser.parse_args()

    arr_1 = init_array('file_1.txt')
    arr_2 = init_array('file_2.txt')

    # st = round(args.value * len(arr_1))
    # sel = np.random.choice(arr_1, 10, False)[0:st] # используем choice а не shuffle 
    # потому что первый возвращает массив а не NoneType
    if len(arr_1) != len(arr_2):
        raise ValueError("Массивы должны быть одинаковой длины") 

    # Создание маски для выбора элементов
    mask = np.random.choice([False, True], size=len(arr_1), p=[1-args.value, args.value])
    # Выбор элементов
    result = np.where(mask, arr_2, arr_1)
    print(result)
