def set_universum(init):
    """
    Позволяет использовать переменную DMPy.universum

    :param init: Iterable or Iterator
    """
    global universum
    universum = set(init)
