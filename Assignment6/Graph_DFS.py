#!/usr/bin/python


import csv
import sys
import numpy as np


def read_graph(fin):
    print("Reading G... ")
    G = []
    inp = open("SCC.txt", "r")
    for line in inp.readlines():
        # add a new sublist
        G.append([])
        # loop over the elemets, split by whitespace
        for i in line.split():
            # convert to integer and append to the last
            # element of the list
            G[-1].append(int(i))
    return G


# If k is equal to one, then we want to look at the reverse graph
def findEdges(G, node, k):
    #item = next((i for i, sublist in enumerate(G) if sublist[0] == node  ), -1);
    return [(i) for i, sublist in enumerate(G) if sublist[k] == node]


def findCC(G, leaders):
    ver = [False] * len(leaders)
    ls = []
    z = range(len(leaders))
    for i in z:
        if (ver[leaders[i] - 1] == False):
            ver[leaders[i] - 1] = True
            ls.append([(j + 1) for j in z if leaders[j] == leaders[i]])
    return ls


def findlengthSCC(leaders):
    z = range(len(leaders))
    cnt = {}
    for i, x in enumerate(leaders):
        # print i, x
        cnt.setdefault(x, 0)
        cnt[x] = cnt[x] + 1

    #sizes = {(x, len(y)) for x, y in cnt.items()};
    # print sizes
    # print cnt
    sizes = list(cnt.values())
    return sizes


def NSort(a, N):
    return np.argsort(a)[::-1][:N]


def buildAdjList(G, num_nodes, k):
    # If k=1, we are considerinf the reversed graph
    ls = {}
    # print ls
    k = k + 1
    for i in range(1, num_nodes + 1):
        ls[i] = []
    for i, sublist in enumerate(G):
        index = sublist[k - 1]
        value = sublist[k - 2]
        ls[index].append(value)

    return ls


def DFS(AdjList, s, mode):
    global t
    global lnode
    explored[s - 1] = True
    stack = [s]
    # print s
    #edges = findEdges(G, s, k);
    #edges = AdjList[s]
    cnt = 0
    if mode == 'direct':
        leaders[s - 1] = lnode
    while stack:
        # print "stack: ", stack
        v = stack[-1]
        if mode == 'direct':
            leaders[v - 1] = lnode
            # print leaders
        # print v
        edges = AdjList[v]
        #cnt = 0;
        # print "Edges of ", v, ": ", edges
        cnt = 0
        if (mode == 'direct'):
            stack.pop()
        for w in edges:

            #v = G[i][m];
            # print w
            if (explored[w - 1] == False):
                cnt = cnt + 1
                # print v
                #DFS(AdjList, v);
                explored[w - 1] = True
                stack.append(w)
                # print "stack: ", stack
                # print explored
        if (cnt == 0 and mode == 'reverse'):
            t = t + 1
            finish[v - 1] = t
            vec_finish[t - 1] = v
            stack.pop()

            # print finish
    # print finish;
    return


# G = [[7,6], [6,3], [3, 4], [3, 11], [4, 5], [11, 4], [5, 11], [2, 5],
#			[9, 2], [9, 11], [1, 8], [1, 9], [8, 9], [10, 9], [10,8], [10, 7], [6, 10]];

#G = [[1,7],[3,9], [2,5],[4,1],[6,3],[5,8],[7,4], [8,2],[6,8],[9,6],[7,9]  ];

#G = [[1,4], [3,6],[5,2],[7,1], [9,3],[8,5],[4,7],[9,7],[2,8],[6,9],[8,6] ];


G = read_graph("SCC.txt")


# print sys.getrecursionlimit();


print "Initializing... "

print len(G)
nnodes = max(max(G))
print "# Nodes: ", nnodes


# Reversed
adjlist = buildAdjList(G, nnodes, 1)


explored = [False] * nnodes

t = 0
finish = [0] * nnodes
vec_finish = [0] * nnodes
leaders = [0] * nnodes
lnode = -1


# print adjlist

print "Running DFS on reverse graph"
for i in xrange(nnodes, 0, -1):
    # print i
    if (explored[i - 1] == False):
        lnode = i
        DFS(adjlist, lnode, 'reverse')

print "Running DFS on direct graph"

# Direct
adjlist = []
adjlist = buildAdjList(G, nnodes, 0)
explored = [False] * nnodes
t = 0

for i in vec_finish[::-1]:
    # print i
    if (explored[i - 1] == False):
        lnode = i
        # print "lnode: ", lnode
        DFS(adjlist, lnode, 'direct')

print "Finding SCC.. "


scc = findlengthSCC(leaders)

sort_index = NSort(scc, 5)

print sort_index

print [scc[i] for i in sort_index]
