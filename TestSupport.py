import unittest
from DMpy.Support import Support
class TestSupport(unittest.TestCase):
  def setUp(self):
    self.support = Support({'котик', 'жабка', 'выдра'})
  def test_forth(self):
    self.assertFalse(self.support.forth('котик') == self.support.forth('жабка'))
    self.assertFalse(self.support.forth('котик') == self.support.forth('выдра'))
    self.assertFalse(self.support.forth('жабка') == self.support.forth('выдра'))
  def test_back(self):
    self.assertFalse(self.support.back(1) == self.support.back(2))
    self.assertFalse(self.support.back(1) == self.support.back(3))
    self.assertFalse(self.support.back(2) == self.support.back(3))
    self.assertEqual(self.support.back(self.support.forth('котик')), 'котик')
    self.assertEqual(self.support.back(self.support.forth('жабка')), 'жабка')
    self.assertEqual(self.support.back(self.support.forth('выдра')), 'выдра')

if __name__ == "__main__":
  unittest.main()
