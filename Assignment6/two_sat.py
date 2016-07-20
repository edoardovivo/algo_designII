import numpy as np
import networkx as nx


def read_2sat(fname):
    first_line = open(fname).readline().strip('\n').split(' ')
    n_vars = int(first_line[0])
    sat_conditions = np.loadtxt(fname, skiprows=1)
    # graph = [(int(x[0]), int(x[1]), x[2]) for x in graph_matrix]

    return (n_vars, sat_conditions.astype(int))


def read_make_graph(fname):
    first_line = open(fname).readline().strip('\n').split(' ')
    n_vars = int(first_line[0])
    sat_conditions = np.loadtxt(fname, skiprows=1)
    graph = {}
    for i in range(n_vars):
        x1 = sat_conditions[i, 0]
        x2 = sat_conditions[i, 1]
        if (int(-x1) in graph):
            graph[int(-x1)].append(int(x2))
        else:
            graph[int(-x1)] = [int(x2)]
        if (int(-x2) in graph):
            graph[int(-x2)].append(int(x1))
        else:
            graph[int(-x2)] = [int(x1)]
    graph = {k: set(v) for k, v in graph.iteritems()}
    return graph


def read_make_graph_nx(fname):
    first_line = open(fname).readline().strip('\n').split(' ')
    n_vars = int(first_line[0])
    sat_conditions = np.loadtxt(fname, skiprows=1)
    graph = nx.DiGraph()
    graph.add_nodes_from([x for x in range(- n_vars, n_vars + 1) if x != 0])
    for i in range(n_vars):
        x1 = int(sat_conditions[i, 0])
        x2 = int(sat_conditions[i, 1])
        graph.add_edge(-x1, x2)
        graph.add_edge(-x2, x1)
    return graph


def check(visited_order):
    visited_opposite = set([-x for x in visited_order])
    s = set(visited_order).intersection(visited_opposite)
    if not s:
        return True
    else:
        print s
        return False


def DFS_connected_components(graph):
    n = len(graph)
    visited = []
    while n > 0:
        # max(graph.keys(), key=lambda x: len(graph[x]))
        start = graph.iterkeys().next()
        visited_order = DFS(graph, start, 'direct')
        # We need to check if -x and x appear in the same connected component.
        if check(visited_order):
            visited.extend(visited_order)
            graph = {k: v for k, v in graph.iteritems() if k not in visited}
            n = len(graph)
            print n, len(visited_order)
        else:
            print "Not Satisfiable!"
            print visited_order
            return False
    return True


def DFS(graph, start, mode):
    # if m=0 we are looking at the reverse graph
    S = []
    visited_order = []
    visited = {k: False for k in graph}
    S.append(start)
    while S:
        u = S.pop()
        if (u in visited and not visited[u]):
            visited_order.append(u)
            visited[u] = True
            if u in graph:
                nodes = graph[u]
            else:
                continue
            S.extend([w for w in nodes if (
                w in visited and not visited[w]) or w not in visited_order])

    return visited_order


def check_graph_scc_nx(components):
    for c in components:
        if len(c) > 1:
            nodes = [node for node in c]
            if not check(nodes):
                print False
                return False
    print True
    return True


def main():
    fnames = ["2sat%d.txt" % x for x in range(1, 7)]
    satisfiable = []
    for name in fnames:
        graph = read_make_graph_nx(name)
        components = nx.strongly_connected_components(graph)
        sat = check_graph_scc_nx(components)
        satisfiable.append(sat)
    return satisfiable


if __name__ == '__main__':
    main()
