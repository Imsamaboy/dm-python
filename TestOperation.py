import unittest
from DMpy.Operations import Operation
class TestOperation(unittest.TestCase):
  def sum_ints(a, b):
    return a + b

  def divide_ints(a, b):
    return a / b

"""__contains__ method is tested here (initialisation by graph)"""
  def test_checking_for_membership_in_operation_initialised_by_graph(self):
    graph1 = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    oper1 = Operation(graph = graph1)
    for key in graph1
      self.assertTrue((key, graph1[key]) in oper1)
      self.assertFalse((key, -1) in oper1)
    self.assertFalse(((1, 3), 1) in oper1)

"""__contains__ method is tested here (initialisation by procedure)"""
  def test_checking_for_membership_in_operation_initialised_by_procedure(self):
    oper1 = Operation(procedure = sum_ints)
    for a in range(10)
      for b in range(10)
        self.assertTrue(((a, b), a+b) in oper1)
        self.assertFalse(((a, b), a+b+1) in oper1)


"""__iter__ method is tested here (initialisation by graph)"""
  def test_iterator_creating_in_operation_initialised_by_graph(self):
    graph1 = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    oper1 = Operation(graph = graph1)

    unchecked_tuples = [key for key in graph1]
    for var_res in oper1
      self.assertEqual(graph1[var_res[0]], var_res[1])
      self.assertTrue(var_res[0] in unchecked_tuples)
      if var_res[0] in unchecked_tuples:
        unchecked_tuples.remove(var_res[0])
      else:
        break


"""__call__ method is tested here (initialisation by graph)"""
  def test_calling_operation_result_in_operation_initialised_by_graph(self):
    graph1 = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    oper1 = Operation(graph = graph1)

    results_of_operations = []
    results_from_graph = []
    for key in graph1
      results_of_operations.append(oper1(key[0], key[1]))
      results_from_graph.append(graph1[key])
    self.assertEqual(results_of_operations, results_from_graph)

"""__call__ method is tested here (initialisation by procedure)"""
  def test_calling_operation_result_in_operation_initialised_by_procedure(self):
    oper2 = Operation(procedure = sum_ints)
    for a in range(100)
      for b in range(100)
        self.assertTrue(oper2(a, b), a+b)
        self.assertFalse(oper2(a, b), a+b+1)


  def test_isTotal(self):
    """need help"""


"""isAssociative method is tested here (initialisation by graph)"""
  def test_associativity_checking_in_operation_initialised_by_graph(self):
    graph1 = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    oper1 = Operation(graph = graph1)
    graph2 = {(0, 0): 0, (0, 1): 2, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    oper2 = Operation(graph = graph2)
    self.assertTrue(oper1.isAssociative())
    self.assertFalse(oper2.isAssociative())

"""isAssociative method is tested here (initialisation by procedure)"""
  def test_associativity_checking_in_operation_initialised_by_procedure(self):
    oper1 = Operation(procedure = sum_ints)
    oper2 = Operation(procedure = divide_ints)
    self.assertTrue(oper1.isAssociative())
    self.assertFalse(oper2.isAssociative())


"""isCommutative method is tested here (initialisation by graph)"""
  def test_commutativity_checking_in_operation_initialised_by_graph(self):
    graph1 = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    oper1 = Operation(graph = graph1)
    graph2 = {(0, 0): 0, (0, 1): 2, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    oper2 = Operation(graph = graph2)
    self.assertTrue(oper1.isCommutative())
    self.assertFalse(oper2.isCommutative())

"""isCommutative method is tested here (initialisation by procedure)"""
  def test_commutativity_checking_in_operation_initialised_by_procedure(self):
    oper1 = Operation(procedure = sum_ints)
    oper2 = Operation(procedure = divide_ints)
    self.assertTrue(oper1.isCommutative())
    self.assertFalse(oper2.isCommutative())

"""hasNeutral method is tested here (initialisation by graph)"""
  def test_neutral_elem_existance_in_operation_initialised_by_graph(self):
    graph1 = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    oper1 = Operation(graph = graph1)
    graph2 = {(0, 0): 0, (0, 1): 2, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    oper2 = Operation(graph = graph2)
    self.assertTrue(oper1.hasNeutral())
    self.assertFalse(oper2.hasNeutral())

"""hasNeutral method is tested here (initialisation by procedure)"""
  def test_neutral_elem_existance_in_operation_initialised_by_procedure(self):
    oper1 = Operation(procedure = sum_ints)
    oper2 = Operation(procedure = divide_ints)
    self.assertTrue(oper1.hasNeutral())
    self.asserttrue(oper2.hasNeutral())

"""hasInverse method is tested here (initialisation by graph)"""
  def test_inverse_elem_existance_in_operation_initialised_by_graph(self):
    graph1 = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}
    oper1 = Operation(graph = graph1)
    graph2 = {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 1}
    oper2 = Operation(graph = graph2)
    self.assertTrue(oper1.hasInverse())
    self.assertFalse(oper2.hasInverse())

"""hasInverse method is tested here (initialisation by procedure)"""
  def test_inverse_elem_existance_in_operation_initialised_by_procedure(self):
    oper1 = Operation(procedure = sum_ints)
    oper2 = Operation(procedure = divide_ints)
    self.assertTrue(oper1.hasInverse())
    self.assertFalse(oper2.hasInverse())