import unittest
from DMpy.Operations import Operation
class TestOperation(unittest.TestCase):
  def sum_ints(a, b):
    return a + b

  def subtract_ints(a, b):
    return a - b

  def test__contains__(self):
    g1 = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    self.oper1 = Operation(graph = g1)
    self.oper2 = Operation(procedure = sum_ints)

    for k in g1
      self.assertTrue((k, g1[k]) in self.oper1)
      self.assertFalse((k, -1) in self.oper1)
    self.assertFalse(((1, 3), 1) in self.oper1)

    for a in range(100)
      for b in range(100)
        self.assertTrue(((a, b), a+b) in self.oper2)
        self.assertFalse(((a, b), a+b+1) in self.oper2)

  def test__iter__(self):
    g1 = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    self.oper1 = Operation(graph = g1)

    unchecked_tuples = [k for k in g1]
    for i in self.oper1
      self.assertEqual(g1[i[0]], i[1])
      unchecked_tuples.remove(i[0])

  def test__call__(self):
    g1 = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    self.oper1 = Operation(graph = g1)
    self.oper2 = Operation(procedure = sum_ints)

    for k in g1
      self.assertEqual(self.oper1(k[0], k[1]), g1[k])

    for a in range(100)
      for b in range(100)
        self.assertTrue(self.oper2(a, b), a+b)
        self.assertFalse(self.oper2(a, b), a+b+1)

  def test_isTotal(self):
    """need help"""

  def test_isAssociative(self):
    g1 = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    self.oper1 = Operation(graph = g1)
    self.oper2 = Operation(procedure = sum_ints)
    g3 = {(0, 0): 0, (0, 1): 2, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    self.oper3 = Operation(graph = g3)
    self.oper4 = Operation(procedure = subtract_ints)

    self.assertTrue(self.oper1.isAssociative())
    self.assertTrue(self.oper2.isAssociative())
    self.assertFalse(self.oper3.isAssociative())
    self.assertFalse(self.oper4.isAssociative())

  def test_isCommutative(self):
    g1 = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    self.oper1 = Operation(graph = g1)
    self.oper2 = Operation(procedure = sum_ints)
    g3 = {(0, 0): 0, (0, 1): 2, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    self.oper3 = Operation(graph = g3)
    self.oper4 = Operation(procedure = subtract_ints)

    self.assertTrue(self.oper1.isCommutative())
    self.assertTrue(self.oper2.isCommutative())
    self.assertFalse(self.oper3.isCommutative())
    self.assertFalse(self.oper4.isCommutative())

  def test_hasNeutral(self):
    g1 = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    self.oper1 = Operation(graph = g1)
    self.oper2 = Operation(procedure = sum_ints)
    g3 = {(0, 0): 0, (0, 1): 2, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    self.oper3 = Operation(graph = g3)
    self.oper4 = Operation(procedure = subtract_ints)

    self.assertTrue(self.oper1.hasNeutral())
    self.assertTrue(self.oper2.hasNeutral())
    self.assertFalse(self.oper3.hasNeutral())
    self.assertTrue(self.oper4.hasNeutral())

  def test_hasInverse(self):
    g1 = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    self.oper1 = Operation(graph = g1)
    self.oper2 = Operation(procedure = sum_ints)
    g3 = {(0, 0): 0, (0, 1): 2, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    self.oper3 = Operation(graph = g3)
    g4 = {(0, 0): 0, (0, 1): 1, (1, 0): 0, (1, 1): 1}

    self.assertTrue(self.oper1.hasInverse())
    self.assertTrue(self.oper2.hasInverse())
    self.assertFalse(self.oper3.hasInverse())
    self.assertFalse(self.oper4.hasInverse())

if __name__ == "__main__":
  unittest.main()
