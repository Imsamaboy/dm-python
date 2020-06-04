""" Модуль для установки универсума """
from DataStructures.Support import Support

# Установим по умолчанию пустой универсум
universum = Support()


def setUniversum(iter=None):
    """
        Инициализация универсума
        :param iter - то, что будем устанавливать в универсум

    """
    global universum
    universum = Support(iter)


def DecartMultiply(deg=2):
    """ Генерируем множество декартого произведения:
            Universum x Universum
    """
    for elem1 in universum:
        for elem2 in universum:
            yield (elem1, elem2)
