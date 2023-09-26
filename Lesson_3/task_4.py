class Inventory:

    def __init__(self, ln):
        print('Class was created')
        self._lst = [None] * ln
        self._ln = ln
        
    def __len__(self):
        return self._ln

    def __str__(self):
        return 'We have amount = ' + str(self._lst)

    def read_val(self, num):
        return self._lst[num-1]

    def write_val(self, num, val):
        self._lst[num-1] = val
        return self

    def __del__(self):
        print('Class was deleted')


if __name__ == "__main__":
    test = Inventory(10)
    print(test)
    test.write_val(2,'MEOW')
    print(test)
    print(test.read_val(2))