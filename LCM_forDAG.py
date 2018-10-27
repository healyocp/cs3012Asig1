from DAGG import graph
 #These can all be  turned into constructor tests


def findLCA(graphh,vertex1,vertex2):
        #reverseG = graph()
        commonAnc=[]
        reverseG= graphh.invert_dict_nonunique()
        print(reverseG)
        vertex1Path=reverseG.bfs_connected_component(vertex1)
        print(vertex1Path)
        vertex2Path=reverseG.bfs_connected_component(vertex2)
        print(vertex2Path)
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


#def locatekeysNotInItems:



"""
def LCA( graphh, a, b):
    dfs_a = graphh.dfs_recursive(a, [])
    #print(dfs_a)

    #print(graphh.edges())
    #print(graphh.vertices())
    #print(dfs_a) basically print out both dictionaries and see what paths they return. and then decide. , i think i need to go through the longer path first

    dfs_b = graphh.dfs_recursive(b, [])
    print(len(dfs_a))
    print(len(dfs_b))
    for i in range(len(dfs_a)):
        #print(len(dfs_a), "b")
        print(repr(i) + " hey")
        #print(range(len(dfs_a)), "a")
            #print (i)
        if dfs_a[i] == dfs_b[i]:
            print(repr(dfs_a[i])+ "bye")
            return dfs_a[i]
    else:
        return -1;

"""

if __name__ == "__main__":
    g = {   1: [2, 3,4],
            2: [4,5],
            3: [4,5],
            4: [6,7],
            5: [6],
            6: [7],
            7: []}

    graphh = graph(g)

    print(findLCA(graphh, 4, 5))
    #print(findLCA(graphh, 1, 2))
    #print(LCA(graphh, 1, 3))
    #print(LCA(graphh, 2, 3))



    #print(LCA(graphh, 6, 7)) fix this: maybe  anested loop is needed
