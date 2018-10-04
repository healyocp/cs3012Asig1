#print("Greetings to internet citizens!")
import unittest
from sys import stdout


class Node (object):

    def __init__(self, val):
        self.val = val
        self.left=None
        self.right = None

#functions to compare dif objects

    def __lt__(self, val):
        return self.val < val
    def __gt__(self, val):
        return self.val > val
    def __eq__(self, val):
        return self.val == val
    def __str__(self):
        return "[Node val: %d]" % self.val

class Tree (object):

    def __init__(self):
        self.root = None # how does tree know that root is node

    def put (self,val):
        self.root=self._put(self.root,val)

    def _put(self,node,val ):
        if node is None:
            node =Node(val)

        if val < node:
            node.left=self._put(node.left,val)
        elif val>node:
            node.right=self._put(node.right,val)
        else:
            node.val=val

        return node

    def get(self,val):
        return self._get(self.root,val)

    def _get(self, node,val):
        while not node is None:
            if val <  node: node =node.left
            elif val > node: node = node.right
            else: return node.val

        return None

    #base case
    def find_common(self,a,b):
        return self._find_common(self.root,a,b)

    #if either a or b match the root val-> this is the lowest common ancestor
    def _find_common(self, node, a, b):

        if node is None:
            return None


        if node.val == a or node.val == b :
            return node.val

        left_lca= self._find_common(node.left,a,b)
        right_lca = self._find_common(node.right,a,b)

        if left_lca and right_lca: # like if they both have values
            return node.val

        return left_lca if left_lca is not None else right_lca



    def node_exists(self, val):
        return self._node_exists(self.root, val)
    def _node_exists(self, node, val):
        return not self._get(node, val) is None




if __name__ == '__main__':


    vals = [30, 8, 52, 3, 20, 10, 29, 62]
    tree = Tree()
    [tree.put(val) for val in vals]
    pairs = [
        (30, 8),
        (3, 29),
        (10, 29),
        (20, 29),
        (3, 62),
        (4, 29),
        (3, 1),
        (8, 3),
        (52, 62)
    ]
    for (a, b) in pairs:
        stdout.write("Common for %d & %d: " % (a, b))
        print (tree.find_common(a, b))
    #unittest.main()



#class Unit_Test_LCM(unittest.TestCase):

    #def test_tree_constructor(self):
    # = Tree()
    #    self.assertEqual(t.root, None)
