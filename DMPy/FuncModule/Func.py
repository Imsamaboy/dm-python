"""
Модуль для работы со всюду определенными (тотальными)
целочисленными функциями
"""

from DataStructures.Support import Support
from collections import defaultdict
from copy import deepcopy
import SetUniversum as SU


class Relation:
    def __init__(self, graph=None, criterion=None):
        """
            :param graph - список пар элементов универсума, которые находятся в отношении
            :param criterion - строит такое отношение R, для которого:
                   aRb <=> существуют такие элементы универсума a, b, что criterion(a, b) == True
        """
        self.criterion = criterion
        self.graph = graph

        if graph:
            self.R = graph

        if criterion:
            # Генерируем множество R по критерию, заданному в качестве функции
            # GenerateR сгенерирует нам множество пар, которые находятся в некотором отношении
            def GenerateR():
                for pair in SU.DecartMultiply():
                    obj1, obj2 = pair
                    if criterion(obj1, obj2):
                        yield pair

            self.R = Support(GenerateR())

    def __iter__(self):
        return iter(self.R)

    def isRefleksive(self):
        """
            Проверка рефлексивности отношения
            Возвращаемое значение: bool
        """
        cur = 0
        for elem in SU.universum:
            if not (elem, elem) in self.R:
                cur += 1
        return cur == 0

    def isNonRefleksive(self):
        """
            Проверка антирефлексивности отношения
            Возвращаемое значение: bool
        """
        return not self.isRefleksive()

    def isSymmetric(self):
        """
            Проверка симметричности отношения
            Возвращаемое значение: bool
        """
        cur = 0
        for elem1 in SU.universum:
            for elem2 in SU.universum:
                if not (elem1, elem2) in self.R or (elem2, elem1) in self.R:
                    pass
                else:
                    cur += 1
        return cur == 0

    def isNonSymmetric(self):
        """
            Проверка антисимметричности отношения
            Возвращаемое значение: bool
        """
        cur = 0
        for elem1 in SU.universum:
            for elem2 in SU.universum:
                if not ((elem1, elem2) in self.R and (elem2, elem1) in self.R) \
                   or elem1 == elem2:
                    pass
                else:
                    cur += 1
        return cur == 0

    def isTransitive(self):
        """
            Проверка транзитивности отношения
            Возвращаемое значение: bool
        """
        cur = 0
        for elem1 in SU.universum:
            for elem2 in SU.universum:
                for elem3 in SU.universum:
                    if not ((elem1, elem2) in self.R and (elem2, elem3) in self.R) \
                       or (elem1, elem3) in self.R:
                        pass
                    else:
                        cur += 1
        return cur == 0

    def isFunctional(self):
        """
            Проверка отношения на свойство функциональности
            Возвращаемое значение: bool
        """
        pass

    def get_Relation(self):
        """ Возвращает объект Support, в котором находятся пары Relation'а """
        return self.R


# Занимаюсь корректированием класса Func
class Func:
    def __init__(self, function_graph: dict):
        """
        :param function_graph: dict
            График отображения как словарь "элемент:образ"
        """
        self.__map = function_graph

    def periodical_closure(self, cycle_closure_stop=False, depth=1, f=None,
                           only_final_layer=True):
        """
        График многократной композиции функции. В случае f=None ожидается, что
        образ множества определения является подмножеством области определения.
        Для удобства добавлена возможность передать непосредственно отображение
        для генерации образа, не включенного в график функции.

        :param cycle_closure_stop: bool
            При True завершает процесс применения композиции, если все
            новые сгенерированные образы уже
        :param depth: int
            Кратность композиции
        :param f: Function (optional)
            Отображение/функция
        :param only_final_layer: bool
            Если True, возвращает только результат применения последней композиции
        :return List[Tuple] пар (элемент, образ)
        """
        mapping = deepcopy(self.__map)
        if not (set(mapping.values()) <= set(mapping.keys())) and f is None:
            raise AssertionError(
                "Невозможно сгенерировать образ. Передайте отображение или "
                "создайте новый объект Func с другим графиком")

        if cycle_closure_stop:
            occurence_checker = defaultdict(lambda: False)

        func_graph = []
        while cycle_closure_stop or depth > 0:
            depth -= 1
            if cycle_closure_stop:
                mapping = {k: v for k, v in mapping.items() if
                           not occurence_checker[(k, v)]}
                if not mapping:
                    return func_graph
                for pair in mapping.items():
                    occurence_checker[pair] = True
            new_graph = list(mapping.items())
            if only_final_layer:
                func_graph = new_graph
            else:
                func_graph += new_graph
            new_keys = mapping.values()
            new_values = [mapping[elem] if elem in mapping.keys() else f(elem)
                          for elem in new_keys]
            mapping = dict(zip(new_keys, new_values))

        return func_graph
