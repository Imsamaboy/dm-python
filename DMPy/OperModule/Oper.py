from DataStructures.Support import Support
from FuncModule.Func import Func

# Реализовываю...
class Oper:
    """ Класс Операций """
    def __init__(self, graph=None):
        """
            Конструктор операции
            :param graph - словарь, проецирующему пары элементов в элементы
        """
        self.graph = graph

    def __contains__(self, item):
        pass

    def __iter__(self):
        pass

    def isTotal(self):
        """ Проверка тотальности """
        pass

    def isAssociative(self):
        """ Проверка ассоциативности """
        pass

    def hasNeutral(self):
        """ Проверка на нейтральный элемент """
        pass

    def hasInverse(self):
        """ Проверка на обратный элемент """
        pass

    def isCommutative(self):
        """ Проверка коммутативности """
        pass

