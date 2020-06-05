import unittest
from DataStructures.Set import Set


class TestSet(unittest.TestCase):
    """ Тестируем класс Set """
    def test_init(self):
        self.set1 = Set([1, 2, 3, 4, 5])
        self.set2 = Set()
        self.set3 = Set([0, 0, 0, 1, 1, 1, 2, 2, 2])
        self.set4 = Set(['Hello', 'I', 'Hate', 'Boulevard Depo!'])
        self.set5 = Set([1.1, 'Hello', 10])

    def test_contains(self):
        """ in """
        self.assertTrue(1 in self.set1)
        self.assertFalse(10 in self.set1)
        self.assertFalse([] in self.set2)
        self.assertFalse('Dota 2' in self.set2)
        self.assertTrue(0 in self.set3)
        self.assertFalse(1000 in self.set3)
        self.assertTrue('I' in self.set4)
        self.assertFalse('Travis Scott' in self.set4)
        self.assertTrue(1.1 in self.set5)
        self.assertFalse('10' in self.set5)

    def test_iter(self):
        """ iter """
        for elem, index in enumerate(self.set1):
            self.assertEqual(elem, self.set1[index])
        for elem, index in enumerate(self.set2):
            self.assertEqual(elem, self.set2[index])
        for elem, index in enumerate(self.set3):
            self.assertEqual(elem, self.set3[index])
        for elem, index in enumerate(self.set4):
            self.assertEqual(elem, self.set4[index])
        for elem, index in enumerate(self.set5):
            self.assertEqual(elem, self.set5[index])

    def test_cup(self):
        """ Cup """
        self.assertEqual(self.set1.cup([2, 228]), Set([1, 2, 3, 4, 5, 228]))
        self.assertEqual(self.set2.cup([]), Set())
        self.assertEqual(self.set3.cup([3]), Set([0, 1, 2, 3]))
        self.assertEqual(self.set4.cup(['Hello']), Set(['Hello', 'I', 'Hate', 'Boulevard Depo!']))
        self.assertEqual(self.set5.cup(['Love']), Set([1.1, 'Hello', 10, 'Love']))

    def test_cap(self):
        """ Cap """
        self.assertEqual(self.set1.cap([1]), Set([1]))
        self.assertEqual(self.set2.cap([10, 230]), Set())
        self.assertEqual(self.set3.cap([3]), Set([3]))
        self.assertEqual(self.set4.cap(['Hello', 'I']), Set(['Hello', 'I']))
        self.assertEqual(self.set5.cap(['Hleb']), Set())


if __name__ == "__main__":
    unittest.main()
