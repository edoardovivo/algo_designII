import csv
import numpy as np


def read_items(fname, nlines=np.inf):
    items = {}
    n = 0
    with open(fname) as f:
        reader = csv.reader(f, delimiter=' ')
        next(reader, None)  # skip the headers
        for row in reader:
            n += 1
            if (n <= nlines ):
                weight = int(row[1])
                value = float(row[0])
                items[int(reader.line_num-1)] = {'weight': weight, 'value': value}
    return items

fname = "/home/edoardo/docker-drive/AlgorithmsDesignII/Assignment3/knapsack1.txt"
#fname = "/home/edoardo/docker-drive/AlgorithmsDesignII/Assignment3/knapsack_big.txt"
items = read_items(fname, nlines=100)
W=10000
n = len(items)
#Solution
A = np.zeros((n, W+1), dtype=float)

for i in range(1, n):
    for x in range(0, W+1):
        ind_weight = x-items[i+1]["weight"]
        if (ind_weight >= 0):
            A[i,x] = max(A[i-1,x], A[i-1, ind_weight] + items[i+1]["value"])
        else:
            A[i,x] = A[i-1,x]

#print A
S = A[n-1,W]
print S

