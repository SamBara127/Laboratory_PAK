class Item:
    def __init__(self, count=3, max_count=16):
        self._count = count
        self._max_count = 16
        
    def update_count(self, val):
        if val <= self._max_count:
            self._count = val
            return True
        else:
            return False
        
    # Свойство объекта. Не принимает параметров кроме self, вызывается без круглых скобок
    # Определяется с помощью декоратора property
    @property
    def count(self):
        return self._count
    
    
    # Ещё один способ изменить атрибут класса
    @count.setter
    def count(self, val):
        self._count = val
        if val <= self._max_count:
            self._counts = val
        else:
            pass
    
    @staticmethod
    def static():
        print('I am function')
    
    @classmethod
    def my_name(cls):
        return cls.__name__

    def __add__(self, num):
        """ Сложение с числом """
        return self._count + num
    
    def __mul__(self, num):
        """ Умножение на число """
        return self._count * num
    
    def __lt__(self, num):
        """ Сравнение меньше """
        return self._count < num
    
    def __len__(self):
        """ Получение длины объекта """
        return self._count

    def __gt__(self, num):
        """a > b"""
        return self._count > num

    def __le__(self, num):
        """a <= b"""
        return self._count <= num

    def __ge__(self, num):
        """a >= b"""
        return self._count >= num

    def __eq__(self, num):
        """a == b"""
        return self._count == num

    def __sub__(self, num):
        """ a - b """
        return self._count - num


        

item = Item(2)
print(item == 1)
# print(item.count * 2)
# ret = item.update_count(8)
# print(ret, item.count)