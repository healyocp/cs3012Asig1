
class graph(object):

    def __init__ (self,graphdict=None):
        if graphdict==None:
            graphdict=dict({}) # what is the purpose of this line , if graphdict is =none in paramtere
        self.__graphdict = graphdict

    def vertices(self):
        return list(self.__graphdict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self,vertex):
        if vertex not in self.__graphdict:
            self.__graphdict[vertex]=[]

    def addEdge(self, edge):
         edge = list (edge)
         if len(edge) != 2 :
            return
         (vertex1, vertex2) = list(edge)
         if vertex1 in self.__graphdict and vertex2 in self.__graphdict:
            self.__graphdict[vertex1].append(vertex2)
         else:
            self.add_vertex(vertex2)
            self.add_vertex(vertex1)
            print(self.__graphdict)
            self.__graphdict[vertex1].append(vertex2)



    def __generate_edges(self):

        edges = []
        for vertex in self.__graphdict:
            print(vertex)
            for neighbour in self.__graphdict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges


    def invert_dict_nonunique(self):
        newGraph=graph()
        first=0
        for k, v in self.__graphdict.items():
            if first==0:
                newGraph.__graphdict.setdefault(k,[])
                first=1
            for x in v:
                newGraph.__graphdict.setdefault(x,[]).append(k)
        print(newGraph)
        return newGraph


    def bfs_connected_component(self, vertex):

        #self.invert_dict_nonunique()
        #print(self.invert_dict_nonunique())
    # keep track of all visited nodes
        explored = []
    # keep track of nodes to be checked
        queue = [vertex]

    # keep looping until there are nodes still to be checked
        while queue:
        # pop shallowest node (first node) from queue

            node = queue.pop(0)
            #print(node)
            if node not in explored:
            # add node to list of checked nodes
                explored.append(node)
                neighbours = self.__graphdict[node]
                #print(self.__graphdict[node])
            # add neighbours of node to queue
                for neighbour in neighbours:
                    queue.append(neighbour)
        return explored

    def findLCA(self,vertex1,vertex2):
                reverseG = graph()
                if self.testCycle()== True:
                    return -1
                else:

                    commonAnc=[]
                    reverseG= self.invert_dict_nonunique()
                #print(reverseG)
                    vertex1Path=reverseG.bfs_connected_component(vertex1)
                #print(vertex1Path)
                    vertex2Path=reverseG.bfs_connected_component(vertex2)
                #print(vertex2Path)
                    found=False
                    for i in range(len(vertex1Path)):
                        for j in range(len(vertex2Path)):
                            if(vertex1Path[i]==vertex2Path[j]):
                                commonAnc.append(vertex1Path[i])
                                found=True


                    if(found):
                        return max(commonAnc)
                    else:
                        return -1

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
            7: []}


dag = graph(g)

#print(g)

#print(nd.edges())

#pathA= nd.bfs_connected_component(5)
"""
e=nd.edges()

print(e)

"""
