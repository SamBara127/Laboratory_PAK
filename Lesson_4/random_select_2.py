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

    if len(arr_1) != len(arr_2):
        raise ValueError("Массивы должны быть одинаковой длины") 

    # Создание массива случайных чисел
    random_numbers = np.random.rand(len(arr_1))
    # Создание массива индексов
    indices = np.where(random_numbers < args.value, 1, 0)
    # Выбор элементов
    result = np.choose(indices, [arr_1, arr_2])
    print(result)
