import unittest
from LCM import Tree

class Test(unittest.TestCase):
    def test_tree_constructor(self):
        t = Tree()
        self.assertEqual(t.root, None)


if __name__ == '__main__':
    unittest.main()
