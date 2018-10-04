import unittest
from LCM import Tree

class Test(unittest.TestCase):
    def test_tree_constructor(self):
        t = Tree()
        self.assertEqual(t.root, None)

    def test_LCM_empty_tree(self):
        t=Tree()
        self.assertEqual(t.find_common(1,2), None)
    def test_LCM_small_tree(self):
        t=Tree()
        vals = [6,3,9]
        for val in vals:
            t.put(val)

        self.assertEqual(t.find_common(3,9), 6)


if __name__ == '__main__':
    unittest.main()
