""" Модуль для работы со всюду определенными (тотальными)
целочисленными функциями"""
from typing import Iterable, List, Tuple

from DataStructures.DMGraph import DMGraph
from DataStructures.Support import Support


class Func:
    """ Класс обертки для взаимодействия с объектами модуля DMPy"""

    def __init__(self, func=lambda x: x):
        """
        :param func: принимаемая функция. По умолчанию стоит тождественное
            отображение
        """
        self.func = func
        self.domain = None

    """TODO: Переделать перегрузить метод __call__ (т.е. создать 2 метода 
    __call__, один для типа 
    Support и другой для всего остального) с помощью декораторов
    
    Туториал: https://www.codementor.io/@arpitbhayani/overload-functions-
    in-python-13e32ahzqt """

    def __call__(self, arg: Support or DMGraph):
        """ __call__ позволяет такой синтаксис:

        new_fun = Func(func=x**2)  # Инициализируем объект класса Func
        result = new_fun(3) # result = 9

    """
        if type(arg) == Support:
            return Support(map(self.func, arg))
        elif type(arg) == DMGraph:
            return DMGraph(self._arg_image_pairs(arg.nodes))
        return self.func(arg)

    """TODO:
    Перегрузить метод (т.е. создать с таким же названием, но другой) 
    (опять же с помощью декоратора) так, чтобы его можно было применять 
    не только к типу Support,
    но и к одному элементу"""

    def generate_orbit(self, domain: Support, depth=3,
                       shape='matrix') -> Support:
        """
    Метод для составления орбит элементов относительно данной функции
    (т.е. f(f(f..(f(x))..)) )

    Если shape='matrix', возвращает Support, элементами которого являются
    другие Support'ы (матрица короче), где return_value[0] - это domain,
    return_value[1] - f(domain), return_value[2] - f(f(domain)) и т.д.

    Если shape='flat', то возвращает одномерный Support,
    где return_value[i] = f(f..(f(domain[i]))
    :param domain: множество действия функции
    :param depth: сколько раз мы применяем функцию к предыдущему результату
    :param shape: 'matrix', 'flat'
    """
        pass

    def _arg_image_pairs(self, arg: Iterable or DMGraph) -> List[Tuple]:
        if type(arg) == Support:
            return [(x, im) for x, im in zip(arg, map(self.func, arg))]
        elif type(arg) == DMGraph:
            return [(x, im) for x, im in
                    zip(arg.nodes, map(self.func, arg.nodes))]

