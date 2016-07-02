import numpy as np
cimport numpy as np


cpdef np.float knapsack(int W, np.ndarray[double, ndim=1] values, np.ndarray[double, ndim=1] weights):
    cdef np.ndarray[double] previous = np.zeros((W + 1,))
    cdef np.ndarray[double] current = np.zeros((W + 1,))
    cdef int i, x, n = len(values)
    cdef int ind_weight = 0
    cdef int weight = 0
    cdef double value = 0
    for i in xrange(1, n):
        weight = int(weights[i])
        value = values[i]
        for x in xrange(0, W + 1):
            ind_weight = x - weight
            if (ind_weight >= 0):
                current[x] = max(previous[x], previous[ind_weight] + value)
            else:
                current[x] = previous[x]
        previous = current.copy()

    return current[-1]
