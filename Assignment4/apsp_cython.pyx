import numpy as np
cimport numpy as np



cpdef float bellman_ford(g1, V, source, n_nodes, n_edges):
    #A = np.zeros((n_edges, n_nodes), dtype=float)

    cdef np.ndarray previous = np.zeros((n_nodes,1))
    cdef np.ndarray current = np.zeros((n_nodes,1))
    cdef np.ndarray w_array = np.array([])
    cdef float min_w = 0
    cdef int i
    for i in xrange(1, n_edges+1):
        for v in V:
            try:
                w_list = g1[v]
            except:
                current[v-1] = np.inf
                continue
            #print w_list
            #for (a,b) in w_list:
            #    np.append([w_array, previous[a-1] + b])
            w_array = np.array([previous[w[0]-1] + w[1] for w in w_list])
            #print w_array
            min_w = w_array.min()
            current[v-1] = min(previous[v-1], min_w)
        # Early stopping
        if ((current == previous).all()):
            break;
        # Check for negative cycles
        if ((current != previous).any() and i == n_edges ):
            # There's a negative cycle
            return -np.inf
        previous = current.copy()

    return current.min()