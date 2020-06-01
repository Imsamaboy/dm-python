from DataStructures import Carrier


class Oper:
    def __init__(self, rule=lambda x, y: x + y):
        self.operation = rule

    def operation_properties(self):
        """ ХЗ если честно"""
        pass

    def partial_evaluation(self, **kwargs):
        pass

