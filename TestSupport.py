import unittest
from DMpy.Support import Support
class TestSupport(unittest.TestCase):

  def test_forth_for_strings(self):
    self.support = Support({'котик', 'жабка', 'выдра'})
    self.assertFalse(self.support.forth('котик') == self.support.forth('жабка'))
    self.assertFalse(self.support.forth('котик') == self.support.forth('выдра'))
    self.assertFalse(self.support.forth('жабка') == self.support.forth('выдра'))

  def test_back_for_strings(self):
    self.support = Support({'котик', 'жабка', 'выдра'})
    self.assertFalse(self.support.back(1) == self.support.back(2))
    self.assertFalse(self.support.back(1) == self.support.back(3))
    self.assertFalse(self.support.back(2) == self.support.back(3))
    self.assertEqual(self.support.back(self.support.forth('котик')), 'котик')
    self.assertEqual(self.support.back(self.support.forth('жабка')), 'жабка')
    self.assertEqual(self.support.back(self.support.forth('выдра')), 'выдра')


  def test_forth_for_numbers(self):
    self.support = Support({11, 22, 33})
    self.assertFalse(self.support.forth(11) == self.support.forth(22))
    self.assertFalse(self.support.forth(11) == self.support.forth(33))
    self.assertFalse(self.support.forth(22) == self.support.forth(33))

  def test_back_for_numbers(self):
    self.support = Support({11, 22, 33})
    self.assertFalse(self.support.back(1) == self.support.back(2))
    self.assertFalse(self.support.back(1) == self.support.back(3))
    self.assertFalse(self.support.back(2) == self.support.back(3))
    self.assertEqual(self.support.back(self.support.forth(11)), 11)
    self.assertEqual(self.support.back(self.support.forth(22)), 22)
    self.assertEqual(self.support.back(self.support.forth(33)), 33)


  def test_forth_for_boolean(self):
    self.support = Support({True, False})
    self.assertFalse(self.support.forth(True) == self.support.forth(False))

  def test_back_for_boolean(self):
    self.support = Support({True, False})
    self.assertFalse(self.support.back(1) == self.support.back(2))
    self.assertEqual(self.support.back(self.support.forth(True)), True)
    self.assertEqual(self.support.back(self.support.forth(False)), False)

  def test_forth_for_mixed_types(self):
    self.support = Support({'котик', 0, True})
    self.assertFalse(self.support.forth('котик') == self.support.forth(0))
    self.assertFalse(self.support.forth('котик') == self.support.forth(True))
    self.assertFalse(self.support.forth(0) == self.support.forth(True))

  def test_back_for_mixed_types(self):
    self.support = Support({'котик', 0, True})
    self.assertFalse(self.support.back(1) == self.support.back(2))
    self.assertFalse(self.support.back(1) == self.support.back(3))
    self.assertFalse(self.support.back(2) == self.support.back(3))
    self.assertEqual(self.support.back(self.support.forth('котик')), 'котик')
    self.assertEqual(self.support.back(self.support.forth(0)), 0)
    self.assertEqual(self.support.back(self.support.forth(True)), True)