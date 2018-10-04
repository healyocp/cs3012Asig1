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

    def test_LCM_larger_tree(self):
        t=Tree()
        vals = [12,4,6,9,1,20,19,2,23,5]
        for val in vals:
            t.put(val)

        self.assertEquals(t.find_common(1,4),4)
        self.assertEquals(t.find_common(1,2),1)
        self.assertEquals(t.find_common(2,5),4)
        self.assertEquals(t.find_common(1,6),4)
        self.assertEquals(t.find_common(6,19),12)
        self.assertEquals(t.find_common(9,19),12)
        self.assertEquals(t.find_common(19,23),20)
        self.assertEquals(t.find_common(4,20),12)
        self.assertEquals(t.find_common(1,23),12)
        self.assertEquals(t.find_common(2,23),12)
        self.assertEquals(t.find_common(5,9),6)
        self.assertEquals(t.find_common(2,19),12)
        self.assertEquals(t.find_common(5,23),12)
        self.assertEquals(t.find_common(20,23),20)
        self.assertEquals(t.find_common(12,20),12)
        self.assertEquals(t.find_common(5,6),6)

    def test_LCM_same_input(self):
        t=Tree()
        vals = [12,4,6,9,1,20,19,2,23,5]
        for val in vals:
            t.put(val)
        self.assertEquals(t.find_common(6,6),6)

    def test_LCM_one_input_no_exist(self):
        t = Tree()
        vals = [12,4,6,9,1,20,19,2,23,5]
        for val in vals:
            t.put(val)
        self.assertEqual(t.find_common(1,11),None)

    def test_single_tree (self):
        t=Tree()
        t.put(2)
        self.assertEqual(t.find_common(2,2),2)
        self.assertEqual(t.find_common(5,5), None)

    def test_get_function (self):
        t=Tree()
        vals = [12,4,6,9,1,20,19,2,23,5]
        for val in vals:
            t.put(val)
        self.assertEqual(t.get(12),12)
        self.assertEqual(t.get(4),4)
        self.assertEqual(t.get(6),6)
        self.assertEqual(t.get(9),9)
        self.assertEqual(t.get(1),1)
        self.assertEqual(t.get(20),20)
        self.assertEqual(t.get(19),19)
        self.assertEqual(t.get(2),2)
        self.assertEqual(t.get(23),23)
        self.assertEqual(t.get(5),5)
        self.assertEqual(t.get(17),None)




if __name__ == '__main__':
    unittest.main()
