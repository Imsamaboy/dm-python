""" Carrier будет стандартный типом данных для наших манипуляций. """

from collections.abc import MutableSet

""" Основная спецификация:
- можно итерироваться по объекту
-
"""


class Carrier(MutableSet):
    """ Стандартный тип данных пакета """

    def __init__(self, init=None):
        """ :param data: инициализация либо через set, либо через int. В случае
         int создает объект из чисел 1..init. Можно не указывать init, тогда
         создастся пустое множество
        Экземпляр класса можно распечатать, используя print

        """
        MutableSet.__init__(self)

        if not init:
            self.__data = set({})
        elif type(init) == int:
            self.__data = {i in range(1, init + 1)}
        else:
            self.__data = set(init)

    ''' MutableSet - абстрактный класс, так что мы должны определить для нашего
     носителя оперции __contains__ ( оператор in),
    __iter__ ( для терирования по множеству в цикле ), __len__ для поддержки
    оператора len, add и discard для операций на множестве
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
        return str(
            self.__data)


""" Реализвция __str__ позволяет распечатать обьект, используя print,
а также преобразовать его в строку"""

