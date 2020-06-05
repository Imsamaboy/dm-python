"""
Модуль для работы со всюду определенными (тотальными)
целочисленными функциями
"""
import SetUniversum as SU
from DataStructures.Support import Support
from DataStructures.Set import Set
from collections import defaultdict
from copy import deepcopy


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
            def generate_r():
                for pair in SU.decart_multiply():
                    obj1, obj2 = pair
                    if criterion(obj1, obj2):
                        yield pair

            self.R = Support(generate_r())

    def __iter__(self):
        return iter(self.R)

    def __contains__(self, item):
        return item in self.R

    def is_refleksive(self):
        """
            Проверка рефлексивности отношения
            Возвращаемое значение:  bool
        """
        cur = 0
        for elem in SU.universum:
            if not (elem, elem) in self.R:
                cur += 1
        return cur == 0

    def is_antirefleksive(self):
        """
            Проверка антирефлексивности отношения
            Возвращаемое значение:  bool
        """
        return not self.is_refleksive()

    def is_symmetric(self):
        """
            Проверка симметричности отношения
            Возвращаемое значение:  bool
        """
        cur = 0
        for elem1 in SU.universum:
            for elem2 in SU.universum:
                if not (elem1, elem2) in self.R or (elem2, elem1) in self.R:
                    pass
                else:
                    cur += 1
        return cur == 0

    def is_antisymmetric(self):
        """
            Проверка антисимметричности отношения
            Возвращаемое значение:  bool
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

    def is_transitive(self):
        """
            Проверка транзитивности отношения
            Возвращаемое значение:  bool
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

    def is_functional(self):
        """
            Проверка отношения на свойство функциональности
            Возвращаемое значение:  bool
        """
        S = Set()
        for (a, b) in self:
            if a in S:
                return False
            S = S.cup(Set({a}))
        return True

    def get_relation(self):
        """ Возвращает объект Support, в котором находятся пары Relation'а """
        return self.R


class Func:
    def __init__(self, function_graph: dict):
        """
        :param function_graph: dict
            График отображения как словарь "элемент:образ"
        """
        self.__map = function_graph

    def __call__(self, arg):
        return self.__map[arg]

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

    def is_surjective(self):
            """ Проверяем сюръективная ли функция """
        temp_map = {value: key for key, value in self.__map.items()}
        return len(Set(temp_map.keys())) == len(self.__map.keys())

    def is_injective(self):
            """ Проверяем инъективная ли функция """
        return len(self.__map.values()) == len(Set((self.__map.values())))
