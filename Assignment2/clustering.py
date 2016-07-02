import csv
import numpy as np
import UnionFind


def read_graph(fname):
    graph = []
    with open(fname) as f:
        reader = csv.reader(f, delimiter=' ')
        next(reader, None)  # skip the headers
        for row in reader:
            node1 = float(row[0])
            node2 = float(row[1])
            cost = float(row[2])
            graph.append((node1, node2, cost))
    return graph


def compute_adj_list(graph):
    adj_list = {}
    for edge in graph:
        if edge[0] not in adj_list.keys():
            adj_list[edge[0]] = set([edge[1]])
        elif edge[0] in adj_list.keys():
            adj_list[edge[0]].add(edge[1])
        if edge[1] not in adj_list.keys():
            adj_list[edge[1]] = set([edge[0]])
        elif edge[1] in adj_list.keys():
            adj_list[edge[1]].add(edge[0])
    return adj_list


def dfs_loop(graph, start):
    '''
    Runs DFS to find loops. Stops when it finds a loop.
    '''
    adj_list = compute_adj_list(graph)
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(adj_list[vertex] - visited)
        else:
            return True
    return False


def kruskal(graph, k):

    graph_nodeset = []
    for edge in graph:
        graph_nodeset.append(int(edge[0]))
        graph_nodeset.append(int(edge[1]))
    graph_nodeset = set(graph_nodeset)
    n_nodes = len(graph_nodeset)
    print n_nodes
    U = UnionFind.UnionFind(n_nodes)
    # print(U)

    # Sort edges
    sorted_edges = sorted(graph, key=lambda x: x[2])  # , reverse=True)
    T = []
    for edge in sorted_edges:
        n = U.size
        print n

        n1 = int(edge[0]) - 1
        n2 = int(edge[1]) - 1
        # Check for loops
        # print U.find(n1)
        # print n2
        # print U.find(n2)
        if (U.find(n1) != U.find(n2)):
            # No loops. Adding the edge to the graph
            if (n == k):
                return T, edge[2]
            else:
                T.append(edge)
                U.union(n1, n2)

    return T, 0

    # Initialize
    #T = []
    # for edge in sorted_edges:
    #    n = len(graph) - len(T)
    #    print n
    #    if (n == k):
    #        print "n, k", n, k
    #        return edge[2]
    #    subgraph = T + [edge]
    #    nodes_subgraph = set(sum([(x[0], x[1]) for x in subgraph], ()))
    #    dfs_list = [dfs_loop(subgraph, node) for node in nodes_subgraph]
    #    if (not any(dfs_list)):
    #        T = subgraph
    # return T


def clustering_small(graph, k):
    return kruskal(graph, k)
