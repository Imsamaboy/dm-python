import pickle


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


if __name__ == "__main__":
    a = {"i": "fds", "sa": "fsa"}
    dump(a, r"ser_test")
    b = load(r"ser_test")
    print(a == b)

    class Pns:
        def __init__(self):
            self.a = 10
            self.b = 20
    a = Pns()

    dump(a, "ser_test")
    b = load("ser_test")
    print(a.a)
    print(b.a)

    from collections import UserList
    from typing import List

    class Carrier(UserList):
        def __init__(self, init: List or int):
            super(Carrier, self).__init__()
            if type(init) == int:
                self.data = [i + 1 in range(init)]
            else:
                self.data = init

    car = Carrier([5, 4, 9, 5])
    dump(car, "ser_test")
    car2 = load("ser_test")
    print(car.data)
    print(car2.data)
