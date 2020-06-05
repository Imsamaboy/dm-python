"""
    Модуль для работы с двуместными функциями (операциями)
"""
import SetUniversum as SU
from DataStructures.Set import Set


class Oper:
    """
        Класс для определения операции:
        f: universum x universum -> universum

        + Есть методы проверки свойств операции
    """
    def __init__(self, graph: dict, procedure=None):
        """
            Конструктор операции
            :param graph - словарь, проецирующему пары элементов в элементы
                   key = (elem1, elem2)
                   graph[key] = elem3
        """
        self.graph = graph
        self.A = Set(graph.keys())
        temp = set()
        for pair in self.A:
            elem1, elem2 = pair
            temp.add(elem1)
            temp.add(elem2)
        self.A = Set(temp)

    def __contains__(self, item):
        return item in self.graph

    def __iter__(self):
        return iter(self.graph)

    def __call__(self, arg1, arg2):
        return self.graph[arg1, arg2]

    def is_total(self):
        """
            Проверка тотальности
            Возвращаемое значение: bool
        """
        for elem1 in SU.universum:
            for elem2 in SU.universum:
                if self.__call__(elem1, elem2) not in self.graph.values():
                    return False
        return True

    def is_associative(self):
        """
            Проверка ассоциативности
            Возвращаемое значение: bool
        """
        for elem1 in SU.universum:
            for elem2 in SU.universum:
                for elem3 in SU.universum:
                    if self.__call__(self.__call__(elem1, elem2), elem3) != \
                       self.__call__(elem1, self.__call__(elem2, elem3)):
                        return False
        return True

    def has_neutral(self):
        """
            Проверка на нейтральный элемент
            Возвращаемое значение: bool
        """
        for elem1 in SU.universum:
            cur = 0
            for elem2 in SU.universum:
                if not (self.__call__(elem1, elem2) == elem2 and
                        self.__call__(elem2, elem1) == elem2):
                    break
                else:
                    cur += 1
            if cur == len(SU.universum):
                return True

    def has_inverse(self):
        """
            Проверка на обратный элемент
            Возвращаемое значение: bool
        """
        cur2 = 0
        for elem1 in SU.universum:
            cur1 = 0
            for elem2 in SU.universum:
                if not (self.__call__(elem1, elem2) == 0 and
                        self.__call__(elem2, elem1) == 0):
                    break
                else:
                    cur1 += 1
            if cur1 == len(SU.universum):
                cur2 += 1
        return cur2 == len(SU.universum)

    def is_commutative(self):
        """
            Проверка коммутативности
            Возвращаемое значение: bool
        """
        for elem1 in SU.universum:
            for elem2 in SU.universum:
                if self.__call__(elem1, elem2) != self.__call__(elem2, elem1):
                    return False
        return True
