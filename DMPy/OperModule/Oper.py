"""
    Модуль для работы с двуместными функциями
"""
from DataStructures.Support import Support
from FuncModule.Func import Func
from DataStructures.Set import Set

# В процессе
class Oper:
    """ Класс Операций """
    def __init__(self, graph: dict):
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

    def isTotal(self):
        """ Проверка тотальности """
        pass

    def isAssociative(self):
        """ Проверка ассоциативности """
        for elem in self.A:
            for pair_1 in self.graph:
                elem1, elem2 = pair_1
                pair_2 = (elem2, elem)
                #print(pair_1, pair_2)
                #print(self.graph[(self.graph[pair_1], elem)])
                #print('Hi')
                #print(self.graph[(elem1, self.graph[pair_2])])
                if self.graph[(self.graph[pair_1], elem)] in self.graph and \
                   self.graph[(elem1, self.graph[pair_2])] in self.graph and \
                   self.graph[(self.graph[pair_1], elem)] == self.graph[(elem1, self.graph[pair_2])]:
                    return True
        return False

    def hasNeutral(self):
        """ Проверка на нейтральный элемент """

    def hasInverse(self):
        """ Проверка на обратный элемент """
        pass

    def isCommutative(self):
        """ Проверка коммутативности """
        for pair in self.graph:
            elem1, elem2 = pair
            print(pair, elem1, elem2)
            print(self.graph[pair])
            print(self.graph[(elem2, elem1)])
            if self.graph[pair] == self.graph[(elem2, elem1)]:
                return True
        return False
