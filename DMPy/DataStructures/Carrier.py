""" Carrier будет дефолтным типом данных для наших операций. """

from collections.abc import MutableSet

""" Основная спецификация: 
- можно итерироваться по объекту
- должен поддерживать оператор [] (элемент по индексу)"""


class Carrier(MutableSet):
    """ Стандартный тип данных пакета """

    def __init__(self, init = None):
        """

        :param data: инициализация либо через set, либо через int. В случае int создает
        лист из чисел 1..init. Можно не указывать init, тогда создастся пустое множество
        Экземпляр класса можно распечатать, используя print
        """

        MutableSet.__init__(self)

        if init == None:
            self.__data = set({})
        elif type(init) == int:
            self.__data = set([i in range(1, init+1)])
        else:
            self.__data = set(init)

    ''' MutableSet - абстрактный класс, так что мы должны определить для нашего носителя оперции __contains__ ( оператор in),
    __iter__ ( для терирования по множеству в цикле ), __len__ для поддержки оператора len, add и discard для операций на множестве
    '''
    def __contains__(self, key):
        return key in self.__data

    def __len__(self):
        return len(self.__data)

    def __iter__(self):
        return iter(self.__data)

    def add(self, key):
        self.__data.add(key)

    def discard(self, key):
        self.__data.discard(key)

    def __str__(self):
        return str(self.__data) #Реализация __str__ позволяет распечатать обьект, используя print, а также преобразовать его в строку

    def copy(self):
        return Carrier(self.__data.copy())


# Тест
if __name__ == "__main__":
    car = Carrier([5, 4, 9, 5])
    print(car._Carrier__data)
    for i in car:
        print(i)
    print(type(Carrier([1, 2, 3])))
    print(5 in car)
    print('foo' in car)
    car.add('crocodile')
    car.discard(4)
    car.discard(4)
    print(car)
    car = Carrier()
    print(car)
    car.add(0)
    print(car)

