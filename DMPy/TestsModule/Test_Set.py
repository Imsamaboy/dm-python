import unittest
from DataStructures.Set import Set


class TestSet(unittest.TestCase):
    """ Тестируем класс Set """
    def setUp(self):
        self.set_with_numbers_1 = Set([1, 2, 3, 4, 5])
        self.empty_set = Set()
        self.set_with_numbers_2 = Set([0, 0, 0, 1, 1, 1, 2, 2, 2])
        self.set_with_strings = Set(['Hello', 'I', 'Hate', 'Boulevard Depo!'])
        self.set_with_mixed_types = Set([1.1, 'Hello', 10])
        self.set_with_bool_types = Set([True, False])

    def test_contains(self):
        """ in """
        self.assertTrue(1 in self.set_with_numbers_1)
        self.assertFalse(10 in self.set_with_numbers_1)
        self.assertFalse([] in self.empty_set)
        self.assertFalse('Dota 2' in self.empty_set)
        self.assertTrue(0 in self.set_with_numbers_2)
        self.assertFalse(1000 in self.set_with_numbers_2)
        self.assertTrue('I' in self.set_with_strings)
        self.assertFalse('Travis Scott' in self.set_with_strings)
        self.assertTrue(1.1 in self.set_with_mixed_types)
        self.assertFalse('10' in self.set_with_mixed_types)
        self.assertTrue(True in self.set_with_bool_types)

    def test_iter(self):
        """ iter """
        for elem, index in enumerate(self.set_with_numbers_1):
            self.assertEqual(elem, self.set_with_numbers_1[index])

        for elem, index in enumerate(self.set_with_numbers_2):
            self.assertEqual(elem, self.set_with_numbers_2[index])

        for elem, index in enumerate(self.empty_set):
            self.assertEqual(elem, self.empty_set[index])

        for elem, index in enumerate(self.set_with_strings):
            self.assertEqual(elem, self.set_with_strings[index])

        for elem, index in enumerate(self.set_with_mixed_types):
            self.assertEqual(elem, self.set_with_mixed_types[index])

        for elem, index in enumerate(self.set_with_bool_types):
            self.assertEqual(elem, self.set_with_bool_types[index])

    def test_cup(self):
        """ Cup """
        self.assertEqual(self.set_with_numbers_1.cup([2, 228]), Set([1, 2, 3, 4, 5, 228]))
        self.assertEqual(self.empty_set.cup([]), Set())
        self.assertEqual(self.set_with_numbers_2.cup([3]), Set([0, 1, 2, 3]))
        self.assertEqual(self.set_with_strings.cup(['Hello']), Set(['Hello', 'I', 'Hate', 'Boulevard Depo!']))
        self.assertEqual(self.set_with_mixed_types.cup(['Love']), Set([1.1, 'Hello', 10, 'Love']))
        self.assertEqual(self.set_with_bool_types.cup([True]), Set([True, False]))

    def test_cap(self):
        """ Cap """
        self.assertEqual(self.set_with_numbers_1.cap([1]), Set([1]))
        self.assertEqual(self.empty_set.cap([10, 230]), Set())
        self.assertEqual(self.set_with_numbers_2.cap([3]), Set([3]))
        self.assertEqual(self.set_with_strings.cap(['Hello', 'I']), Set(['Hello', 'I']))
        self.assertEqual(self.set_with_mixed_types.cap(['Hleb']), Set())
        self.assertEqual(self.set_with_bool_types.cap([True]), Set([True]))


if __name__ == "__main__":
    unittest.main()
