'''
In this programming problem you'll code up Prim's
minimum spanning tree algorithm.
Download the text file below.

edges.txt
This file describes an undirected graph with integer edge costs.
It has the format

[number_of_nodes] [number_of_edges]

[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]

[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]

...

For example, the third line of the file is "2 3 -8874",
indicating that there is an edge connecting vertex #2
and vertex #3 that has cost -8874.

You should NOT assume that edge costs are positive,
nor should you assume that they are distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph.
You should report the overall cost of a minimum spanning tree --- an integer,
which may or may not be negative --- in the box below.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn)
time implementation of Prim's algorithm should work fine.
OPTIONAL: For those of you seeking an additional challenge,
try implementing a heap-based version. The simpler approach,
which should already give you a healthy speed-up,
is to maintain relevant edges in a heap (with keys = edge costs).
The superior approach stores the unprocessed vertices in the heap,
as described in lecture. Note this requires a heap that supports deletions,
and you'll probably need to maintain some kind of mapping between vertices
and their positions in the heap.

SOLUTION: -3612829
'''


import csv
import numpy as np


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


def find_mst(graph, s):
    graph_nodeset = set(sum([(x[0], x[1]) for x in graph], ()))
    X = set([s])
    T = []

    remaining = graph_nodeset - X
    # Start while loop
    while remaining:
        # Find all the edges connecting X and G-X
        candidate_edges = [(n1, n2, w) for n1, n2, w in graph if (
            n1 in X and n2 in remaining) or (n2 in X and n1 in remaining)]
        # Find the minimum weight edge
        winning_edge = sorted(candidate_edges, key=lambda x: x[2])[0]
        # Add the new vertex to the set X and add its weight to T
        X.add(winning_edge[0])
        X.add(winning_edge[1])
        T.append(winning_edge)
        remaining = graph_nodeset - X
    return T


def main():
    fname = "/home/edoardo/docker-drive/AlgorithmsDesignII/Assignment1/edges.txt"
    graph = read_graph(fname)
    # Starting node
    s = graph[0][0]

    T = find_mst(graph, s)

    total_cost = np.array([x[2] for x in T]).sum()

    print "Total cost: ", total_cost


if __name__ == "__main__":
    main()
