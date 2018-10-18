graph = {'A':['C', 'D', 'E'],
        'B': ['C'],
        'C': ['D', 'E'],
        'D':['E']}

#print(graph['C'])


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        print(start)
        print(graph[start])
        if node not in path:
            print(node + "m")
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None
#print find_path(graph, 'A','E')
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
#print(find_all_paths(graph,'A','E'))
def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest


print(find_path(graph, 'A', 'E'))
