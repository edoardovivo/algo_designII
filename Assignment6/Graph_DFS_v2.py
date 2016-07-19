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


def NSort(a, N):
    return np.argsort(a)[::-1][:N]


def DFS(graph, start, mode, visited=None):
    global t
    global lnode
    # if m=0 we are looking at the reverse graph
    if (mode == 'direct'):
        k = 0
        m = 1
    elif (mode == 'reverse'):
        k = 1
        m = 0
    if visited is None:
        visited = set()
    visited.add(start)
    #leaders[s-1] = lnode
    for next in graph[start] - visited:
        DFS(graph, next, mode, visited)
    return visited

    #t = t+1;
    #finish[s-1] = t;
    #vec_finish[t-1] = s;
    # print finish;


# G = [[7,6], [6,3], [3, 4], [3, 11], [4, 5], [11, 4], [5, 11], [2, 5],
#			[9, 2], [9, 11], [1, 8], [1, 9], [8, 9], [10, 9], [10,8], [10, 7], [6, 10]];

#G = [[1,7],[3,9], [2,5],[4,1],[6,3],[5,8],[7,4], [8,2],[6,8],[9,6],[7,9]  ];


G = {	1: set([7]),
      2: set([5]),
      3: set([9]),
      4: set([1]),
      5: set([8]),
      6: set([3, 8]),
      7: set([4, 9]),
      8: set([2]),
      9: set([6])
      }


#G = read_graph("SCC.txt");
for i in G.keys:

    # print sys.getrecursionlimit();


print "Initializing... "

print len(G)
nnodes = len(G)
print "# Nodes: ", nnodes


t = 0
finish = [0] * nnodes
vec_finish = [0] * nnodes
leaders = [0] * nnodes
lnode = -1

vis = DFS(G, 1, 'direct')

print vis


# print "Running DFS on reverse graph"
# for i in xrange(nnodes, 0, -1):
#	if (expl[i-1] == False):
#		lnode=i;
#		DFS(G,lnode,'reverse');


# print "Running DFS on direct graph"
#expl = [False]*nnodes;
# t=0;
# for i in vec_finish[::-1]:
#	if (expl[i-1] == False):
#		lnode=i;
#		DFS(G,lnode,'direct');


#scc = findCC(G, leaders);
# print leaders
#scclen = map(len, scc);

#scclensort = NSort(scclen, 5);

# print scc;

# for x in scclensort:
#	print scclen[x]
