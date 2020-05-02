"""Модуль для операций """


class Oper:
    def __init__(self, rule=lambda x, y: x + y):
        self.operation = rule

    def operation_properties(self):
        """ ХЗ если честно"""
        pass

    def partial_evaluation(self, **kwards):
        """ Тут тоже хз, в помощь functools.partial(почитайте доки) и в гугле 'partial evaluation'"""
