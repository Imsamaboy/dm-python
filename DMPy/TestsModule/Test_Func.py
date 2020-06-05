import unittest
import setUniversum as SU
from FuncModule.Func import Func


class TestFunc(unittest.TestCase):
    """ Тестирование класса Func """
    def setUp(self):
        map_with_numbers_1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 10: 10}
        map_with_numbers_2 = {1: 2, 2: 3, 3: 4, 4: 1, 5: 2, 6: 3, 10: 4}
        map_with_numbers_3 = {1: 1, 2: 1}
        empty_map = {}
        map_with_numbers_with_strings = {1: 'Кот', 'Рыба': 1}
        map_with_strings = {'Рыба': 'Perfect', 'Meat': 'Bad', 'Perfect': 'Рыба', 'Bad': 'Meat'}
        map_with_bool_types = {True: True, False: False}

        self.func_with_numbers_1 = Func(function_graph=map_with_numbers_1)
        self.func_with_numbers_2 = Func(function_graph=map_with_numbers_2)
        self.func_with_numbers_3 = Func(function_graph=map_with_numbers_3)
        self.empty_func = Func(function_graph=empty_map)
        self.func_with_numbers_with_strings = Func(function_graph=map_with_numbers_with_strings)
        self.func_with_strings = Func(function_graph=map_with_strings)
        self.func_with_bool = Func(function_graph=map_with_strings)

    def test_is_surjective(self):
        """ Проверка сюръективности """
        self.assertEqual(self.func_with_numbers_1.is_surjective(), True)
        self.assertEqual(self.func_with_numbers_2.is_surjective(), False)
        self.assertEqual(self.func_with_numbers_3.is_surjective(), False)
        self.assertEqual(self.empty_func.is_surjective(), False)
        self.assertEqual(self.func_with_numbers_with_strings.is_surjective(), False)
        self.assertEqual(self.func_with_strings.is_surjective(), True)
        self.assertEqual(self.func_with_bool.is_surjective(), True)

    def test_is_injective(self):
        """ Проверка инъективности """
        self.assertEqual(self.func_with_numbers_1.is_injective(), True)
        self.assertEqual(self.func_with_numbers_2.is_injective(), False)
        self.assertEqual(self.func_with_numbers_3.is_injective(), False)
        self.assertEqual(self.empty_func.is_injective(), False)
        self.assertEqual(self.func_with_numbers_with_strings.is_injective(), False)
        self.assertEqual(self.func_with_strings.is_injective(), True)
        self.assertEqual(self.func_with_bool.is_injective(), True)


if __name__ == "__main__":
    unittest.main()
