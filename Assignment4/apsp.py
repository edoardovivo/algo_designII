'''
In this assignment you will implement one or more algorithms for the all-pairs shortest-path problem. Here are data files describing three graphs:

g1.txt
g2.txt
g3.txt
The first line indicates the number of vertices and edges, respectively. Each subsequent line describes an edge (the first two numbers are its tail and head, respectively) and its length (the third number). NOTE: some of the edge lengths are negative. NOTE: These graphs may or may not have negative-cost cycles.

Your task is to compute the "shortest shortest path". Precisely, you must first identify which, if any, of the three graphs have no negative cycles. For each such graph, you should compute all-pairs shortest paths and remember the smallest one (i.e., compute min .... d(u,v), where d(u,v) denotes the shortest-path distance from u to v).

If each of the three graphs has a negative-cost cycle, then enter "NULL" in the box below. If exactly one graph has no negative-cost cycles, then enter the length of its shortest shortest path in the box below. If two or more of the graphs have no negative-cost cycles, then enter the smallest of the lengths of their shortest shortest paths in the box below.

OPTIONAL: You can use whatever algorithm you like to solve this question. If you have extra time, try comparing the performance of different all-pairs shortest-path algorithms!

'''

import numpy as np
from apsp_cython import *


def find_edges(graph, v):
    weights = np.array([x[2] for x in graph if x[1] == v])
    i = np.argmin(weights)
    return ()


def read_graph(fname):
    first_line = open(fname).readline().strip('\n').split(' ')
    n_nodes = int(first_line[0])
    n_edges = int(first_line[1])
    graph_matrix = np.loadtxt(fname, skiprows=1)
    #graph = [(int(x[0]), int(x[1]), x[2]) for x in graph_matrix]

    return (n_nodes, n_edges, graph_matrix)


def main():
    # fname ="g1.txt"

    # V = set([int(i) for x in graph for i in (x[0], x[1])]) - set([source])

    # g1 = {}
    # for x in graph:
    #     if (x[1]) in g1:
    #         g1[x[1]].append((x[0], x[2]))
    #     else:
    #         g1[x[1]] = [(x[0], x[2])]

    # sp = bellman_ford(g1, V, source, n_nodes, n_edges)
    fnames = ["g1.txt", "g2.txt", "g3.txt"]
    sp = []
    for f in fnames:
        n_nodes, n_edges, graph_matrix = read_graph(f)
        sp.append(floyd_warshall(graph_matrix, n_nodes, n_edges))

    print sp


if __name__ == "__main__":
    main()
