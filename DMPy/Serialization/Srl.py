import pickle
from DataStructures.Carrier import Carrier


def dump(something, filename):
    """
    Функция сериализации объектов в памяти,
    принимаемые аргументы - сам объект и Ваше название для файла.
    """
    with open(rf'{filename}.pickle', 'wb') as file:
        pickle.dump(something, file)


def load(filename):
    """ Загрузка объекта из памяти, принимаемый аргумент - название файла."""
    with open(rf'{filename}.pickle', 'rb') as file:
        return pickle.load(file)

# if __name__ == "__main__":
#     a = {"i": "fds", "sa": "fsa"}
#     dump(a, r"ser_test")
#     b = load(r"ser_test")
#     print(a == b)
#
#
#     class Pns:
#         def __init__(self):
#             self.a = 10
#             self.b = 20
#
#
#     a = Pns()
#
#     dump(a, "ser_test")
#     b = load("ser_test")
#     print(a.a)
#     print(b.a)
#
#     car = Carrier([5, 4, 9, 5])
#     dump(car, "ser_test")
#     car2 = load("ser_test")
#     print(car)
#     print(car2)
