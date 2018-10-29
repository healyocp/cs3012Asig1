from DAGG import graph

x=range(3)
print(x)

for i in range(3):
    print i

def testCycle(self):
    """Return True if the directed graph g has a cycle.
    g must be represented as a dictionary mapping vertices to
    iterables of neighbouring vertices. For example:

    >>> cyclic({1: (2,), 2: (3,), 3: (1,)})
    True
    >>> cyclic({1: (2,), 2: (3,), 3: (4,)})
    False

    """
    path = set()
    visited = set()

    def visit(vertex):
        if vertex in visited:
            return False
        visited.add(vertex)
        path.add(vertex)
        for neighbour in g.get(vertex, ()):
            if neighbour in path or visit(neighbour):
                return True
        path.remove(vertex)
        return False

    return any(visit(v) for v in g)


g = {   1: [2, 3,4],
            2: [4, 5],
            3: [4,5],
            4: [6,7],
            5: [6],
            6: [7],
            7: [1]}


dag = graph(g)
x= testCycle(dag)
print(x)
