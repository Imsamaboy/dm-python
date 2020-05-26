""" Support будет стандартный типом данных для наших манипуляций. """
from collections import OrderedDict


class Support:
    """
       Контейнер, хранящий пары "число:элемент" и "элемент:число".
       По умолчанию наружу отдаются только элементы. Уникальность
       элементов гарантируется.
    """

    def __init__(self, init=None):

        """
        :param init: Iterable[Hashable] or None. В случае None создается
            "пустое множество"
        """

        if not init:
            self.__data = OrderedDict()
            self.__reversed_data = OrderedDict()
        else:
            init_unique = list(OrderedDict.fromkeys(init))
            # Лучший способ удалить дупликаты, сохраняя оригинальный порядок
            zipped_pairs = zip([i for i in range(1, len(init_unique) + 1)],
                               init_unique)
            self.__data = OrderedDict(
                (num, elem) for num, elem in zipped_pairs)
            self.__reversed_data = OrderedDict(
                (elem, num) for num, elem in zipped_pairs)

    def forth(self, elem):
        return self.__reversed_data[elem]

    def back(self, num):
        return self.__data[num]

    def __len__(self):
        return len(self.__data)

    def __iter__(self):
        for elem in dict.values(self.__data):
            yield elem

    def __str__(self):  # Красивая распечатка
        return 'Support' + str(dict.values(self.__data)). \
            replace("dict_values", "")
