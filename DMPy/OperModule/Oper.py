from DataStructures import Carrier


class Oper:
    def __init__(self, rule=lambda x, y: x + y):
        self.operation = rule

    def operation_properties(self):
        """ ХЗ если честно"""
        pass

    def partial_evaluation(self, **kwargs):
        """ Тут тоже хз, в помощь functools.partial(почитайте доки) и в гугле 'partial evaluation'"""

# class Relation:
#     def __init__(self, logic_relation=lambda x, y: x == y):
#
