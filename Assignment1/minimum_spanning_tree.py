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
        candidate_edges = [(n1, n2, w) for n1,n2,w in graph if (n1 in X and n2 in remaining) or (n2 in X and n1 in remaining)]
        # Find the minimum weight edge
        winning_edge = sorted(candidate_edges, key=lambda x: x[2])[0]
        # Add the new vertex to the set X and add its weight to T
        X.add(winning_edge[0])
        X.add(winning_edge[1])
        T.append(winning_edge)
        remaining = graph_nodeset - X
    return T

fname = "/home/edoardo/docker-drive/AlgorithmsDesignII/Assignment1/edges.txt"
graph = read_graph(fname)
# Starting node
s = graph[0][0]

T = find_mst(graph, s)

total_cost = np.array([x[2] for x in T]).sum()

print "Total cost: ", total_cost