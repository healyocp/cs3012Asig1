import unittest
from DAGG import graph

class TestStringMethods(unittest.TestCase):

    def test_constructor(self):
        g = graph()
        self.assertEqual(g.vertices(), [])
        self.assertEqual(g.edges(), [])

    def test_constructor_notnull(self):
        g = {   1: [2, 3],
                2: [4, 5],
                3: [5],
                4: [6,7],
                5: [6],
                6: [7],
                7: []}

        graphh = graph(g)
        self.assertEqual(graphh.vertices(), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(graphh.edges(), [{1, 2}, {1, 3}, {2, 4}, {2, 5}, {3, 5}, {4, 6},{4,7}, {5, 6}, {6, 7}])

    def test_add_vertex(self):
        graphh = graph()

        graphh.add_vertex(3)
        self.assertEqual(graphh.vertices(), [3])

    def test_add_edge(self):
        g = {   1: [2, 3,4],
                2: [4, 5],
                3: [5],
                4: [6],
                5: [6],
                6: [7],
                7: []}

        graphh = graph(g)
        graphh.addEdge({5, 7})
        self.assertEqual(graphh.edges(), [{1, 2}, {1, 3},{1,4}, {2, 4}, {2, 5}, {3, 5}, {4, 6}, {5, 6},{5,7}, {6, 7}])

        #graphh.add_edge({2, 2})
        #graphh.add_edge({2, 3, 4})

    def test_add_new_edge(self):
        g = {   1: [2, 3],
                2: [4, 5],
                3: [5],
                4: [6],
                5: [6],
                6: [7],
                7: []}


        graphh = graph(g)
        graphh.addEdge({1, 12})
        self.assertEqual(graphh.edges(), [{1, 2}, {1, 3}, {1, 12}, {2, 4}, {2, 5}, {3, 5}, {4, 6}, {5, 6}, {6, 7}])
        self.assertEqual(graphh.vertices(), [1, 2, 3, 4, 5, 6, 7, 12])

unittest.main(exit=False)

if __name__ == '__main__':
    unittest.main()
