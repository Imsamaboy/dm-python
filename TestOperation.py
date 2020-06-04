import unittest
from DMpy.Operations import Operation
class TestOperation(unittest.TestCase):
  def sum_ints(a, b):
    return a + b

  def divide_ints(a, b):
    return a / b

  def test__contains__for_graph_initialisation(self):
    g1 = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    self.oper1 = Operation(graph = g1)
    for k in g1
      self.assertTrue((k, g1[k]) in self.oper1)
      self.assertFalse((k, -1) in self.oper1)
    self.assertFalse(((1, 3), 1) in self.oper1)

  def test__contains__for_procedure_initialisation(self):
    self.oper1 = Operation(procedure = sum_ints)
    for a in range(10)
      for b in range(10)
        self.assertTrue(((a, b), a+b) in self.oper1)
        self.assertFalse(((a, b), a+b+1) in self.oper1)

  def test__iter__(self):
    g1 = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    self.oper1 = Operation(graph = g1)

    unchecked_tuples = [k for k in g1]
    for i in self.oper1
      self.assertEqual(g1[i[0]], i[1])
      self.assertTrue(i[0] in unchecked_tuples)
      if i[0] in unchecked_tuples:
        unchecked_tuples.remove(i[0])
      else:
        break

  def test__call__for_graph_initialisation(self):
    g1 = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    self.oper1 = Operation(graph = g1)

    results_of_operations = []
    results_from_graph = []
    for k in g1
      results_of_operations.append(self.oper1(k[0], k[1]))
      results_from_graph.append(g1[k])
    self.assertEqual(results_of_operations, results_from_graph)

  def test__call__for_procedure_initialisation(self):
    self.oper2 = Operation(procedure = sum_ints)
    for a in range(100)
      for b in range(100)
        self.assertTrue(self.oper2(a, b), a+b)
        self.assertFalse(self.oper2(a, b), a+b+1)

  def test_isTotal(self):
    """need help"""

  def test_isAssociative_for_graph_initialisation(self):
    g1 = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    self.oper1 = Operation(graph = g1)
    g2 = {(0, 0): 0, (0, 1): 2, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    self.oper2 = Operation(graph = g2)
    self.assertTrue(self.oper1.isAssociative())
    self.assertFalse(self.oper2.isAssociative())

  def test_isAssociative_for_procedure_initialisation(self):
    self.oper1 = Operation(procedure = sum_ints)
    self.oper2 = Operation(procedure = divide_ints)
    self.assertTrue(self.oper1.isAssociative())
    self.assertFalse(self.oper2.isAssociative())


  def test_isCommutative_for_graph_initialisation(self):
    g1 = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    self.oper1 = Operation(graph = g1)
    g2 = {(0, 0): 0, (0, 1): 2, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    self.oper2 = Operation(graph = g2)
    self.assertTrue(self.oper1.isCommutative())
    self.assertFalse(self.oper2.isCommutative())

  def test_isCommutative_for_procedure_initialisation(self):
    self.oper1 = Operation(procedure = sum_ints)
    self.oper2 = Operation(procedure = divide_ints)
    self.assertTrue(self.oper1.isCommutative())
    self.assertFalse(self.oper2.isCommutative())


  def test_hasNeutral_for_graph_initialisation(self):
    g1 = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    self.oper1 = Operation(graph = g1)
    g2 = {(0, 0): 0, (0, 1): 2, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    self.oper2 = Operation(graph = g2)
    self.assertTrue(self.oper1.hasNeutral())
    self.assertFalse(self.oper2.hasNeutral())

  def test_hasNeutral_for_procedure_initialisation(self):
    self.oper1 = Operation(procedure = sum_ints)
    self.oper2 = Operation(procedure = divide_ints)
    self.assertTrue(self.oper1.hasNeutral())
    self.asserttrue(self.oper2.hasNeutral())


  def test_hasInverse_for_graph_initialisation(self):
    g1 = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    self.oper1 = Operation(graph = g1)
    g2 = {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 1}
    self.oper2 = Operation(graph = g2)
    self.assertTrue(self.oper1.hasInverse())
    self.assertFalse(self.oper2.hasInverse())

  def test_hasInverse_for_procedure_initialisation(self):
    self.oper1 = Operation(procedure = sum_ints)
    self.oper2 = Operation(procedure = divide_ints)
    self.assertTrue(self.oper1.hasInverse())
    self.assertFalse(self.oper2.hasInverse())