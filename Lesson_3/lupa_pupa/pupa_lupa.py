

class Pupa:

    def __init__(self):
        self._lst = []
        self._lst2 = []
        self._lstr = []
        self._ls = []
        self._st = '1'
        self._val = 0


    def take_salary(self, inc):
        self._val += inc

    
    def do_work(self, fn_1, fn_2):

        with open(fn_1, 'r') as f:
            while(self._st != ''):
                self._st = f.readline()
                if self._st != '\n':
                    self._st = self._st[:-1]
                    self._ls = self._st.split(' ')
                    self._lst.append(self._ls)
        self._lst.pop()
        self._ls = []
        self._st = '1'

        with open(fn_2, 'r') as f:
            while(self._st != ''):
                self._st = f.readline()
                if self._st != '\n':
                    self._st = self._st[:-1]
                    self._ls = self._st.split(' ')
                    self._lst2.append(self._ls)
        self._lst2.pop()

        print("Результат класса Pupa:")
        print("----------------------")

        for i in range(len(self._lst)):
            for j in range(len(self._lst[0])):
                print(int(self._lst[i][j])+int(self._lst2[i][j]), end=' ')
            print('\n')
        print("----------------------")


class Lupa:

    def __init__(self):
        self._lst = []
        self._lst2 = []
        self._lstr = []
        self._ls = []
        self._st = '1'
        self._val = 0

    
    def take_salary(self, inc):
        self._val += inc


    def do_work(self, fn_1, fn_2):

        with open(fn_1, 'r') as f:
            while(self._st != ''):
                self._st = f.readline()
                if self._st != '\n':
                    self._st = self._st[:-1]
                    self._ls = self._st.split(' ')
                    self._lst.append(self._ls)
        self._lst.pop()
        self._ls = []
        self._st = '1'

        with open(fn_2, 'r') as f:
            while(self._st != ''):
                self._st = f.readline()
                if self._st != '\n':
                    self._st = self._st[:-1]
                    self._ls = self._st.split(' ')
                    self._lst2.append(self._ls)
        self._lst2.pop()

        print("Результат класса Lupa:")
        print("----------------------")

        for i in range(len(self._lst)):
            for j in range(len(self._lst[0])):
                print(int(self._lst[i][j])-int(self._lst2[i][j]), end=' ')
            print('\n')
        print("----------------------")


class Accountant:

    def __init__(self, pupa, lupa):
        self.pupa = pupa
        self.lupa = lupa


    def give_salary(self, cl: Lupa):
        cl.take_salary(2)


    def give_salary(self, cl: Pupa):
        cl.take_salary(2)

    
if __name__ == '__main__':
    lupa = Lupa()
    pupa = Pupa()
    lupa.do_work('lupa_pupa\matrix_1.txt', 'lupa_pupa\matrix_2.txt')
    sal = Accountant(pupa, lupa)
    sal.give_salary(pupa)
    print(pupa._val)
    # pass