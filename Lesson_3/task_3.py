

class Fruit:

    def __init__(self, amount, native):
        print('Создание класса съедобных фруктов...')
        self._amount = amount
        self._native = []
        self._native.append(native)

    @property
    def amount(self):
        return self._amount

    def native(self, num):
        return self._native[num-1]

    def native_country(self, num):
        return self._native[num-1][1]

    def native_fruit(self, num):
        return self._native[num-1][0]

    def __add__(self, num):
        """ Сложение с числом """
        self._amount + num
        return self

    def __iadd__(self, num):
        """ Сложение с числом """
        self._amount += num
        return self
    
    def __mul__(self, num):
        """ Умножение на число """
        self._amount * num
        return self
    
    def __lt__(self, num):
        """ Сравнение меньше """
        self._amount < num
        return self
    
    def __len__(self):
        """ Получение длины объекта """
        return self._amount

    def __str__(self):
        """ Вызов как строки """
        return 'We have amount = ' + str(self._amount) 

    def __del__(self):
        print('Удаление класса...')


class NotFruit:

    def __init__(self, amount, native):
        print('Создание класса съедобных не фруктов...')
        self._amount = amount
        self._native = []
        self._native.append(native)

    @property
    def amount(self):
        return self._amount

    def native(self, num):
        return self._native[num-1]

    def native_country(self, num):
        return self._native[num-1][1]

    def native_nofruit(self, num):
        return self._native[num-1][0]

    def __add__(self, num):
        """ Сложение с числом """
        return self._amount + num
    
    def __mul__(self, num):
        """ Умножение на число """
        return self._amount * num
    
    def __lt__(self, num):
        """ Сравнение меньше """
        return self._amount < num
    
    def __len__(self):
        """ Получение длины объекта """
        return self._amount

    def __str__(self):
        """ Вызов как строки """
        return 'We have amount = ' + str(self._amount) 

    def __del__(self):
        print('Удаление класса...')


if __name__ == "__main__":
    fruit = Fruit(1, ['Apple', 'China'])
    print(fruit)
    print(fruit.native_country(1))
    print(fruit.native_fruit(1))
    del fruit
    no_fruit = NotFruit(1, ['Meet', 'USA'])
    print(no_fruit)
    print(no_fruit.native_country(1))
    print(no_fruit.native_nofruit(1))
    del no_fruit
