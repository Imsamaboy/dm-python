import unittest
from Serialization.Srl import *


class SerializationTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_support(self):
        a = Support([1, "lol", 3, "hehehehheheheh", 6, True, 1])
        support_to_json(a, "file1")
        b = support_from_json("file1")
        self.assertEqual(a.__dict__, b.__dict__)

    def test_func(self):
        a = Func({1: "2", 23214: "lololol", 4: 1, True: 2, 1: False})
        function_to_json(a, "file2")
        b = function_from_json("file2")
        self.assertEqual(a.__dict__, b.__dict__)

    def test_list(self):
        a = [1, 2, 3, 4, 5]
        dump_to_json(a, "file3")
        b = load_from_json("file3")
        self.assertEqual(a, b)

    def test_oper(self):
        a = Oper(lambda x_x, o_o: x_x * o_o + o_o)
        operation_to_json(a, "file4")
        b = operation_from_json("file4")
        first_arg = a.operation(2, 3)
        sec_arg = b.operation(2, 3)
        self.assertEqual(first_arg, sec_arg)


if __name__ == "__main__":
    unittest.main()
