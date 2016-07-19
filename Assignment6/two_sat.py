import numpy as np


def read_2sat(fname):
    first_line = open(fname).readline().strip('\n').split(' ')
    n_vars = int(first_line[0])
    sat_conditions = np.loadtxt(fname, skiprows=1)
    # graph = [(int(x[0]), int(x[1]), x[2]) for x in graph_matrix]

    return (n_vars, sat_conditions.astype(int))


def make_graph(n_vars, sat_conditions):
    
    keys = [x for x in range(-n_vars, n_vars+1) if x != 0]
    graph = {k: [] for k in keys}
    for i in range(n_vars):
        x1 = sat_conditions[i, 0]
        x2 = sat_conditions[i, 1]
        try:
            graph[-x1].append(x2)
        except:
            graph[-x1] = [x2]
        try:
            graph[-x2].append(x1)
        except:
            graph[-x2] = [x1]
    
    graph = {k: set(v) for k,v in graph.iteritems()}
    return graph



def DFS_connected_components(graph):
    visited = {k: False for k in graph}
    nodes_to_visit = graph.keys()
    connected_components = {}
    while nodes_to_visit:
        # I want to start the search from the most connected node
        start = max(nodes_to_visit, key=lambda x: len(graph[x]))
        if (len(graph[start]) == 0):
            visited[start] = True
            connected_components[start] = [start]
            nodes_to_visit.remove(start)
        else:
            #start = nodes_to_visit[0]
            visited, visited_order = DFS(graph, start, 'direct', visited=visited)
            connected_components[start] = visited_order
            # We need to check if -x and x appear in the same connected component.
            # If so, we need to check if they are in the same STRONGLY connected component.
        nodes_to_visit = [node for node, v in visited.iteritems() if not v]
        print len(nodes_to_visit)
    return connected_components


def DFS(graph, start, mode, visited=None):
    # if m=0 we are looking at the reverse graph
    S = []
    visited_order = []
    S.append(start)
    while S:
        u = S.pop()
        if (not visited[u]):
            visited[u] = True
            visited_order.append(u)
            try:
                nodes = graph[u]
            except:
                continue
            S.extend((w for w in nodes if not visited[w]))

    #if (mode == 'direct'):
    #    k = 0
    #    m = 1
    #elif (mode == 'reverse'):
    #    k = 1
    #    m = 0
    #if visited is None:
    #    visited = set()
    #visited.add(start)
    #leaders[s-1] = lnode
    #for next in graph[start] - visited:
    #    DFS(graph, next, mode, visited)
    return visited, visited_order


def main():
    fname = "2sat6.txt"
    n_vars, sat_conditions = read_2sat(fname)
    graph = make_graph(n_vars, sat_conditions)
    return graph


if __name__ == '__main__':
    main()
