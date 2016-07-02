cimport numpy as np
import numpy as np

cpdef double knapsack(np.ndarray values, np.ndarray weights):
    cdef int W = 10000
    cdef np.ndarray[double] previous = np.zeros((W+1,))
    cdef np.ndarray[double] current = np.zeros((W+1,))
    cdef int i, x, n = len(values)
    cdef int ind_weight = 0
    for i in xrange(1,n):
        weight = weights[i]
        value = values[i]
        for x in xrange(0,W+1):
            ind_weight = x - weight
            if (ind_weight >= 0):
                current[x] = max(previous[x], previous[ind_weight] + value)
            else:
                current[x] = previous[x]
        previous = current.copy()

    return current[-1]