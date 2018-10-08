import unittest

from b import multiply
class TestUM(unittest.TestCase):


    def setUp(self):
            pass

    def test_numbers_3_4(self):
        t = multiply()
        self.assertEqual( t.multiplyfun(3,4), 12)


if __name__ == '__main__':
    unittest.main()
