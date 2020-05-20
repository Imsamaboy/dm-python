""" Модуль для работы со множествами """

from DataStructures.Carrier import Carrier


def Union(*carriers) -> Carrier:
    carriers = iter(carriers)
    result_python_set = next(carriers)._Carrier__data.copy()
    for carrier in carriers:
        result_python_set.update( carrier._Carrier__data )
    return Carrier( result_python_set )

def Intersection(*carriers) -> Carrier:
    carriers = iter(carriers)
    result_python_set = next(carriers)._Carrier__data.copy()
    for carrier in carriers:
        result_python_set.intersection_update( carrier._Carrier__data )
    return Carrier( result_python_set )

def Difference(first: Carrier, *others) -> Carrier:
    result_python_set = first._Carrier__data.copy()
    for other in others:
        result_python_set.update_difference( other._Carrier__data )
    return Carrier( result_python_set )

def Symmetric_difference(first: Carrier, second: Carrier) -> Carrier:
    return Carrier( first._Carrier__data.symmetric_difference( second._Carrier__data ) )

if __name__ == "__main__":
    a = Carrier({1, 2, 3})
    b = Carrier({3, 5, 'a'})
    print(Union(a, b))
    print(Intersection(a, b))
    print(Symmetric_difference(a, b))
