from DAGG import graph
 #These can all be  turned into constructor tests


def findLCA(graphh,vertex1,vertex2):
        #reverseG = graph()
        commonAnc=[]
        reverseG= graphh.invert_dict_nonunique()
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
    print(findLCA(graphh, 1, 2))
    #print(LCA(graphh, 6, 7)) fix this: maybe  anested loop is needed
