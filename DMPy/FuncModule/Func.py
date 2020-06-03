""" Модуль для работы со всюду определенными (тотальными)
целочисленными функциями"""

from DataStructures.Support import Support
from collections import defaultdict
from copy import deepcopy


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
