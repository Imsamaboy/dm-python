import unittest
from DMpy.Support import Support
class TestSupport(unittest.TestCase):

  def test_forth_for_strings(self):
    support = Support({'котик', 'жабка', 'выдра'})
    self.assertFalse(support.forth('котик') == support.forth('жабка'))
    self.assertFalse(support.forth('котик') == support.forth('выдра'))
    self.assertFalse(support.forth('жабка') == support.forth('выдра'))

  def test_back_for_strings(self):
    support = Support({'котик', 'жабка', 'выдра'})
    self.assertFalse(support.back(1) == support.back(2))
    self.assertFalse(support.back(1) == support.back(3))
    self.assertFalse(support.back(2) == support.back(3))
    self.assertEqual(support.back(support.forth('котик')), 'котик')
    self.assertEqual(support.back(support.forth('жабка')), 'жабка')
    self.assertEqual(support.back(support.forth('выдра')), 'выдра')


  def test_forth_for_numbers(self):
    support = Support({11, 22, 33})
    self.assertFalse(support.forth(11) == support.forth(22))
    self.assertFalse(support.forth(11) == support.forth(33))
    self.assertFalse(support.forth(22) == support.forth(33))

  def test_back_for_numbers(self):
    support = Support({11, 22, 33})
    self.assertFalse(support.back(1) == support.back(2))
    self.assertFalse(support.back(1) == support.back(3))
    self.assertFalse(support.back(2) == support.back(3))
    self.assertEqual(support.back(support.forth(11)), 11)
    self.assertEqual(support.back(support.forth(22)), 22)
    self.assertEqual(support.back(support.forth(33)), 33)


  def test_forth_for_boolean(self):
    support = Support({True, False})
    self.assertFalse(support.forth(True) == support.forth(False))

  def test_back_for_boolean(self):
    support = Support({True, False})
    self.assertFalse(support.back(1) == support.back(2))
    self.assertEqual(support.back(support.forth(True)), True)
    self.assertEqual(support.back(support.forth(False)), False)

  def test_forth_for_mixed_types(self):
    support = Support({'котик', 0, True})
    self.assertFalse(support.forth('котик') == support.forth(0))
    self.assertFalse(support.forth('котик') == support.forth(True))
    self.assertFalse(support.forth(0) == support.forth(True))

  def test_back_for_mixed_types(self):
    support = Support({'котик', 0, True})
    self.assertFalse(support.back(1) == support.back(2))
    self.assertFalse(support.back(1) == support.back(3))
    self.assertFalse(support.back(2) == support.back(3))
    self.assertEqual(support.back(support.forth('котик')), 'котик')
    self.assertEqual(support.back(support.forth(0)), 0)
    self.assertEqual(support.back(support.forth(True)), True)