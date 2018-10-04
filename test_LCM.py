import unittest
from LCM import Tree

class Test(unittest.TestCase):
    def test_tree_constructor(self):
        t = Tree()
        self.assertEqual(t.root, None)

    def test_LCM_empty_tree(self):
        t=Tree()
        self.assertEqual(t.find_common(1,2), None)
    


if __name__ == '__main__':
    unittest.main()
