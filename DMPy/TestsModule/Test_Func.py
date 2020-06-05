import unittest
import setUniversum as SU
from FuncModule.Func import Func


class TestFunc(unittest.TestCase):
    """ Тестирование класса Func """
    def setUp(self):
        map_1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 10: 10}
        map_2 = {1: 2, 2: 3, 3: 4, 4: 1, 5: 2, 6: 3, 10: 4}
        map_3 = {}
        map_4 = {1: 1, 2: 1}
        map_5 = {1: 'Кот', 'Рыба': 1}
        map_6 = {'Рыба': 'Perfect', 'Meat': 'Bad', 'Perfect': 'Рыба', 'Bad': 'Meat'}
        self.f1 = Func(function_graph=map_1)
        self.f2 = Func(function_graph=map_2)
        self.f3 = Func(function_graph=map_3)
        self.f4 = Func(function_graph=map_4)
        self.f5 = Func(function_graph=map_4)
        self.f6 = Func(function_graph=map_4)

    def test_is_surjective(self):
        """ Проверка сюръективности """
        self.assertEqual(self.f1.is_surjective(), True)
        self.assertEqual(self.f2.is_surjective(), False)
        self.assertEqual(self.f3.is_surjective(), False)
        self.assertEqual(self.f4.is_surjective(), False)
        self.assertEqual(self.f5.is_surjective(), False)
        self.assertEqual(self.f6.is_surjective(), True)

    def test_is_injective(self):
        """ Проверка инъективности """
        self.assertEqual(self.f1.is_injective(), True)
        self.assertEqual(self.f2.is_injective(), False)
        self.assertEqual(self.f3.is_injective(), False)
        self.assertEqual(self.f4.is_injective(), False)
        self.assertEqual(self.f5.is_injective(), False)
        self.assertEqual(self.f6.is_injective(), True)


if __name__ == "__main__":
    unittest.main()
