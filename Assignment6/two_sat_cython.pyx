cimport numpy as np
import numpy as np
from cpython cimport bool


cdef bool check(list visited_order):
    cdef set visited_opposite = set([-x for x in visited_order])
    cdef set s = set(visited_order).intersection(visited_opposite)
    if not s:
        return True
    else:
        return False


cpdef bool DFS_connected_components(dict graph):
    cdef int n = len(graph)
    cdef list visited = []
    cdef int start = 0
    cdef list visited_order = []
    cdef bool result = False
    while n > 0:
        start = graph.iterkeys().next() #max(graph.keys(), key=lambda x: len(graph[x]))
        visited_order = DFS(graph, start)
        # We need to check if -x and x appear in the same connected component.
        if check(visited_order):
            visited.extend(visited_order)
            graph = {k: v for k, v in graph.iteritems() if k not in visited}
            n = len(graph)
            #print n, len(visited_order)
        else:
            #print "Not Satisfiable!"
            #print visited_order
            return result
    result = True
    return result


cdef list DFS(dict graph, int start):
    # if m=0 we are looking at the reverse graph
    cdef list S = []
    cdef list visited_order = []
    cdef dict visited = {k: False for k in graph}
    cdef set nodes = set([])
    cdef int w = 0
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
            S.extend([w for w in nodes if (w in visited and not visited[w]) or w not in visited_order])

    return visited_order