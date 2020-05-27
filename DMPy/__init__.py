from DataStructures.Support import Support
from FuncModule.Func import Func
from Serialization import Srl
from Visualisation import Visualisation


def set_universum(init):
    """
    Позволяет использовать переменную DMPy.universum

    :param init: Iterable or Iterator
    """
    global universum
    universum = set(init)
