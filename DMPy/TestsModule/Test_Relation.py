import unittest
import setUniversum as SU
from FuncModule.Func import Relation


class TestRelation(unittest.TestCase):
    """ Тестирование класса Relation """
    def setUp(self):
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

        self.relation_1 = Relation(criterion=is_bigger)
        self.relation_2 = Relation(criterion=is_bigger_or_equal)
        self.relation_3 = Relation(criterion=is_equal)
        self.relation_4 = Relation(criterion=is_not_equal)

    def test_is_refleksive(self):
        """ Проверка рефлексивности отношения """
        self.assertFalse(self.relation_1.is_refleksive())
        self.assertFalse(self.relation_2.is_refleksive())
        self.assertTrue(self.relation_3.is_refleksive())
        self.assertTrue(self.relation_4.is_refleksive())

    def test_is_antirefleksive(self):
        """ Проверка антирефлексивности отношения"""
        self.assertTrue(self.relation_1.is_antirefleksive())
        self.assertTrue(self.relation_2.is_antirefleksive())
        self.assertFalse(self.relation_3.is_antirefleksive())
        self.assertFalse(self.relation_4.is_antirefleksive())

    def test_is_symmetric(self):
        """ Проверка симметричности отношения"""
        self.assertFalse(self.relation_1.is_symmetric())
        self.assertTrue(self.relation_2.is_symmetric())
        self.assertTrue(self.relation_3.is_symmetric())
        self.assertTrue(self.relation_4.is_symmetric())

    def test_is_antisymmetric(self):
        """ Проверка антисимметричности отношения """
        self.assertTrue(self.relation_1.is_antisymmetric())
        self.assertFalse(self.relation_2.is_antisymmetric())
        self.assertFalse(self.relation_3.is_antisymmetric())
        self.assertFalse(self.relation_4.is_antisymmetric())

    def test_is_transitive(self):
        """ Проверка транзитивности отношения """
        self.assertTrue(self.relation_1.is_transitive())
        self.assertTrue(self.relation_2.is_transitive())
        self.assertTrue(self.relation_3.is_transitive())
        self.assertTrue(self.relation_4.is_transitive())


if __name__ == "__main__":
    unittest.main()
