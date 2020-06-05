import unittest
import setUniversum as SU
from FuncModule.Func import Func
from FuncModule.Func import Relation


class TestRelation(unittest.TestCase):
    """ Тестирование класса Relation """
    def test_init(self):
        def is_bigger(self, num1, num2):
            """ Отношение ">" """
            return SU.universum.back(num1) > SU.universum.back(num2)

        def is_bigger_or_equal(self, num1, num2):
            """ Отношение ">=" """
            return SU.universum.back(num1) >= SU.universum.back(num2)

        def is_equal(self, num1, num2):
            """ Отношение "==" """
            return SU.universum.back(num1) == SU.universum.back(num2)

        def is_not_equal(self, num1, num2):
            """ Отношение "!=" """
            return SU.universum.back(num1) != SU.universum.back(num2)

        self.R1 = Relation(criterion=is_bigger)
        self.R2 = Relation(criterion=is_bigger_or_equal)
        self.R3 = Relation(criterion=is_equal)
        self.R4 = Relation(criterion=is_not_equal)

    def test_is_refleksive(self):
        """ Проверка рефлексивности отношения """
        self.assertTrue(self.R1.is_refleksive())
        self.assertTrue(self.R2.is_refleksive())
        self.assertTrue(self.R3.is_refleksive())
        self.assertTrue(self.R4.is_refleksive())
        self.assertFalse(self.R1.is_refleksive())
        self.assertFalse(self.R2.is_refleksive())
        self.assertFalse(self.R3.is_refleksive())
        self.assertFalse(self.R4.is_refleksive())

    def test_is_antirefleksive(self):
        """ Проверка антирефлексивности отношения"""
        self.assertTrue(self.R1.is_antirefleksive())
        self.assertTrue(self.R2.is_antirefleksive())
        self.assertTrue(self.R3.is_antirefleksive())
        self.assertTrue(self.R4.is_antirefleksive())
        self.assertFalse(self.R1.is_antirefleksive())
        self.assertFalse(self.R2.is_antirefleksive())
        self.assertFalse(self.R3.is_antirefleksive())
        self.assertFalse(self.R4.is_antirefleksive())

    def test_is_symmetric(self):
        """ Проверка симметричности отношения"""
        self.assertTrue(self.R1.is_symmetric())
        self.assertTrue(self.R2.is_symmetric())
        self.assertTrue(self.R3.is_symmetric())
        self.assertTrue(self.R4.is_symmetric())
        self.assertFalse(self.R1.is_symmetric())
        self.assertFalse(self.R2.is_symmetric())
        self.assertFalse(self.R3.is_symmetric())
        self.assertFalse(self.R4.is_symmetric())

    def test_is_antisymmetric(self):
        """ Проверка антисимметричности отношения """
        self.assertTrue(self.R1.is_antisymmetric())
        self.assertTrue(self.R2.is_antisymmetric())
        self.assertTrue(self.R3.is_antisymmetric())
        self.assertTrue(self.R4.is_antisymmetric())
        self.assertFalse(self.R1.is_antisymmetric())
        self.assertFalse(self.R2.is_antisymmetric())
        self.assertFalse(self.R3.is_antisymmetric())
        self.assertFalse(self.R4.is_antisymmetric())

    def test_is_transitive(self):
        """ Проверка транзитивности отношения """
        self.assertTrue(self.R1.is_transitive())
        self.assertTrue(self.R2.is_transitive())
        self.assertTrue(self.R3.is_transitive())
        self.assertTrue(self.R4.is_transitive())
        self.assertFalse(self.R1.is_transitive())
        self.assertFalse(self.R2.is_transitive())
        self.assertFalse(self.R3.is_transitive())
        self.assertFalse(self.R4.is_transitive())


class TestFunc(unittest.TestCase):
    """ Тестирование класса Func """
    def test_init(self):
        map_1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 10: 10}
        map_2 = {1: 2, 2: 3, 3: 4, 4: 1, 5: 2, 6: 3, 10: 4}
        map_3 = {}
        map_4 = {1: 1, 2: 1}
        self.f1 = Func(function_graph=map_1)
        self.f2 = Func(function_graph=map_2)
        self.f3 = Func(function_graph=map_3)
        self.f4 = Func(function_graph=map_4)

    def test_is_surjective(self):
        """ Проверка сюръективности """
        self.assertEqual(self.f1.is_surjective(), True)
        self.assertEqual(self.f2.is_surjective(), False)
        self.assertEqual(self.f3.is_surjective(), False)
        self.assertEqual(self.f4.is_surjective(), False)

    def test_is_injective(self):
        """ Проверка инъективности """
        self.assertEqual(self.f1.is_injective(), True)
        self.assertEqual(self.f2.is_injective(), False)
        self.assertEqual(self.f3.is_injective(), False)
        self.assertEqual(self.f4.is_injective(), False)


if __name__ == "__main__":
    unittest.main()
