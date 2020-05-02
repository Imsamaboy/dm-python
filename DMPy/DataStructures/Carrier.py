""" Carrier будет дефолтным типом данных для наших операций. """

from collections import UserList
from typing import List

# от UserList удобнее наследоваться, погуглите

""" TODO: Возможно, наследоваться от листа - не лучшая идея, и стоит переделать класс Carrier
Основная спецификация: 
- можно итерироваться по объекту
- должен поддерживать оператор [] (элемент по индексу)"""


class Carrier(UserList):
    """ Класс наследуется от UserList.

    Не оч понимаю, какие тут должны быть фичи, но придумать что-то можно"""

    def __init__(self, init: List or int):
        """

        :param data: инициализация либо через list, либо через int. В случае int создает
        лист из чисел 1..init
        """

        super(Carrier, self).__init__()
        if type(init) == int:
            self.data = [i + 1 in range(init)]
        else:
            self.data = init


# Тест
if __name__ == "__main__":
    print(type([1, 2, 3]) == list)
    car = Carrier([5, 4, 9, 5])
    print(car.data)
    for i in car:
        print(i)
    print(car[-1])
    print(type(Carrier([1, 2, 3])))
