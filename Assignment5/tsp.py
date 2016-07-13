'''
In this assignment you will implement one or more algorithms for the traveling salesman problem, such as the dynamic programming algorithm covered in the video lectures. Here is a data file describing a TSP instance.

tsp.txt
The first line indicates the number of cities. Each city is a point in the plane, and each subsequent line indicates the x- and y-coordinates of a single city.

The distance between two cities is defined as the Euclidean distance --- that is, two cities at locations (x,y) and (z,w) have distance .... between them.

In the box below, type in the minimum cost of a traveling salesman tour for this instance, rounded down to the nearest integer.

OPTIONAL: If you want bigger data sets to play with, check out the TSP instances from around the world here. The smallest data set (Western Sahara) has 29 cities, and most of the data sets are much bigger than that. What's the largest of these data sets that you're able to solve --- using dynamic programming or, if you like, a completely different method?

HINT: You might experiment with ways to reduce the data set size. For example, trying plotting the points. Can you infer any structure of the optimal solution? Can you use that structure to speed up your algorithm?
'''


import numpy as np
import itertools
import UnionFind


def read_graph(fname):
    first_line = open(fname).readline().strip('\n').split(' ')
    n_cities = int(first_line[0])
    graph_matrix = np.loadtxt(fname, skiprows=1)
    # graph = [(int(x[0]), int(x[1]), x[2]) for x in graph_matrix]

    return (n_cities, graph_matrix)


def compute_distances(n_cities, graph_matrix):
    distances = {}
    for i in range(1, n_cities + 1):
        for j in range(i + 1, n_cities + 1):
            p1 = graph_matrix[i - 1, :]
            p2 = graph_matrix[j - 1, :]
            d = np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
            distances[(i, j)] = d
            distances[(j, i)] = d
    return distances


def tsp(n_cities, graph_matrix, distances):
    AS = []
    # Base case
    AS.append((set([1]), 1, 1))  # Set S, j, and value
    for i in range(2, n_cities + 1):
        AS.append((set([i]), 1, np.inf))

    # Loop start
    for m in range(2, n_cities + 1):
        # Find all sets of size m containing 1
        S = [set(i) for i in itertools.combinations(range(1, n_cities + 1), m)
             if 1 in i]
        for s in S:
            for j in s:
                if (j != 1):
                    s1 = s - set([j])
                    # FIND all A[S-{j}]
                    A = [item[2] + distances[(item[1], j)]
                         for item in AS if item[0] == s1 and item[1] != j]
                    a = min(A)
                    AS.append((s, j, a))

    AS_final = min([item[2] + distances[(item[1], 1)] for item in AS
                    if item[0] == set(range(1, n_cities + 1))])
    return AS_final


def kruskal(graph, k):

    graph_nodeset = []
    for edge in graph:
        graph_nodeset.append(int(edge[0]))
        graph_nodeset.append(int(edge[1]))
    graph_nodeset = set(graph_nodeset)
    n_nodes = len(graph_nodeset)
    U = UnionFind.UnionFind(n_nodes)

    # Sort edges
    sorted_edges = sorted(graph, key=lambda x: x[2])  # , reverse=True)
    T = []
    for edge in sorted_edges:
        n = U.size

        n1 = int(edge[0]) - 2
        n2 = int(edge[1]) - 2
        # Check for loops
        # print U.find(n1)

        # print U.find(n2)
        if (U.find(n1) != U.find(n2)):
            # No loops. Adding the edge to the graph
            if (n == k):
                return U, T, edge[2]
            else:
                T.append(edge)
                U.union(n1, n2)
    return U, T





def main():
    fname = "tsp_.txt"
    n_cities, graph_matrix = read_graph(fname)
    distances = compute_distances(n_cities, graph_matrix)
    AS = tsp(n_cities, graph_matrix, distances)
    print AS
    

if __name__ == "__main__":
    main()
