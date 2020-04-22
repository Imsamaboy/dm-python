""" Carrier будет дефолтным типом данных для наших операций. """

from collections import UserList

# от UserList удобнее наследоваться, погуглите

""" TODO: Возможно, наследоваться от листа - не лучшая идея, и стоит переделать класс Carrier
Основная спецификация: 
- можно итерироваться по объекту
- должен поддерживать оператор [] (элемент по индексу)"""


class Carrier(UserList):
    """ Класс наследуется от UserList.

    Не оч понимаю, какие тут должны быть фичи, но придумать что-то можно"""

    def __init__(self, data=[], n=None):
        UserList.__init__(self)
        if n:  # по дефолту - мн-во 1..n
            self.data = [i for i in range(n)]
        else:
            self.data = data


# Тест
if __name__ == "__main__":
    for i in Carrier([1, 2, 3]):
        print(i)
