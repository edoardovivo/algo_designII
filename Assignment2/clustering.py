'''
In this programming problem and the next you'll code up the clustering algorithm from lecture for computing a max-spacing k-clustering.

Download the text file below.

clustering1.txt
This file describes a distance function (equivalently, a complete graph with edge costs). It has the following format:

[number_of_nodes]

[edge 1 node 1] [edge 1 node 2] [edge 1 cost]

[edge 2 node 1] [edge 2 node 2] [edge 2 cost]

...

There is one edge (i,j) for each choice of 1≤i<j≤n, where n is the number of nodes.

For example, the third line of the file is "1 3 5250", indicating that the distance between nodes 1 and 3 (equivalently, the cost of the edge (1,3)) is 5250. You can assume that distances are positive, but you should NOT assume that they are distinct.

Your task in this problem is to run the clustering algorithm from lecture on this data set, where the target number k of clusters is set to 4. What is the maximum spacing of a 4-clustering?

ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!


'''

import csv
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


def main():
    fname = "clustering1.txt"
    graph = read_graph(fname)
    T, max_spacing = clustering_small(graph, 4)
    print "Max spacing: ", max_spacing


if __name__ == "__main__":
    main()
