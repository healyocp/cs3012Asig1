class graph(object):

def _init_ (self,graphdict=None):
        if graphdict==None:
            graphdict()={}
        self.__graphdict = graphdict

def vertices(self):

        return self.__graphdict.keys())

def edges(self):
        return self.__get_edges()

def add_vertex(self,vertex):
        if vertex not in self.__graphdict:
            self.__graphdict[vertex]=[]

def addEdge(self, edge):
        edge=set(edge)
        (vertex1,vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

def __generate_edges(self):

        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges


def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res



def dfs_recursive(self, vertex, path):
        path += [vertex]

        for neighbor in self.__graph_dict[vertex]:
            if neighbor not in path:
                path = self.dfs_recursive(neighbor, path)

        return path
            
