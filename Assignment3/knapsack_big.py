import csv
import numpy as np
import knapsack_cython as knc

def is_better(item1, item2):
    v1 = item1["value"]
    v2 = item2["value"]
    w1 = item1["weight"]
    w2 = item2["weight"]

    if (v1 > v2 and w1 < w2):
        # Item 1 is better
        return True
    else:
        return False


def is_worse(item1, item2):
    v1 = item1["value"]
    v2 = item2["value"]
    w1 = item1["weight"]
    w2 = item2["weight"]

    if (v1 <= v2 and w1 >= w2):
        return True
    else:
        return False


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




fname = "/home/edoardo/docker-drive/AlgorithmsDesignII/Assignment3/knapsack_big.txt"
items = read_items(fname)
W = 1200000
n = len(items)

# Number of elements the item i is striclty better than
counts = []
for i in xrange(1,n+1):
    counts.append((i, sum([is_better(items[i], items[j]) for j in xrange(i+1,n)])))

# Sorted 
counts = sorted(counts, key=lambda x: x[1], reverse=True)

# Find the smallest set of good items that exceed the maximum weight W
s = 0
i = 1
while (s <= W):
    s += items[counts[i][0]]["weight"]
    i += 1

n_elem = i
golden_items = [x[0] for x in counts[0:i]]
print [items[i]["weight"] for i in golden_items]

# For each item, check if it is strictly worse than ALL elements in golden_items
# If it is worse, then exclude it from the analysis
for i in xrange(1,n):
    if all([is_worse(items[i], items[gold]) for gold in golden_items]):
        items.pop(i)


values = np.array([x["value"] for x in items.values()])
weights = np.array([x["weight"] for x in items.values()])

#sol = knc.knapsack(values, weights)
#print sol



# Run the algorithm on the subset of items
#n = len(items)
#previous = np.zeros((W+1,))
#current = np.zeros((W+1,))
#
#
#solution = [0]
#for (i,item) in items.iteritems():
#    weight = item["weight"]
#    value = item["value"]
#    for x in xrange(0,W+1):
#        ind_weight = x - weight
#        if (ind_weight >= 0):
#            current[x] = max(previous[x], previous[ind_weight] + value)
#        else:
#            current[x] = previous[x]
#    previous = current.copy()
#
#S = current[-1]
#print S