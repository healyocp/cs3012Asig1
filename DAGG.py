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
            for neighbour in self.__graphdict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges


    def __str__(self):
        res = "vertices: "
        for k in self.__graphdict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res



    def dfs_recursive(self, vertex, path):
        path += [vertex]

        for neighbor in self.__graphdict[vertex]:
            #print(self.__graphdict[vertex])
            #print( neighbor)
            if neighbor not in path:
                path = self.dfs_recursive(neighbor, path)
        print(path)
        return path

    def invert_dict_nonunique(self):
        newdict=dict()
        for k, v in self.__graphdict.items():
            for x in v:
                newdict.setdefault(x,[]).append(k)
        return newdict


g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["d", "e"],
          "d" : [ ],
          "e" : ["f"],
          "f" : []
      }

# check print and add funcitons work

dag = graph(g)
print(g)
nd= dag.invert_dict_nonunique()
print(nd)
#a = dag.__str__()



#print(a)

"""
print("Vertices of graph:")
print(dag.vertices())
print("Edges of graph:")
print(dag.edges())
print("Add vertex:")
dag.add_vertex("z")
print("Vertices of graph:")
print(dag.vertices())
print("Add an edge:")
dag.addEdge({"a","z"})
print("Vertices of graph:")
print(dag.vertices())
print("Edges of graph:")
print(dag.edges())
print('Adding an edge {"x","y"} with new vertices:')
dag.addEdge({"x","y"})
print("Vertices of graph:")
print(dag.vertices())
print("Edges of graph:")
print(dag.edges())
"""
