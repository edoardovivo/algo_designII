'''
This problem also asks you to solve a knapsack instance, but a much bigger one.

Download the text file below.

knapsack_big.txt
This file describes a knapsack instance, and it has the following format:

[knapsack_size][number_of_items]

[value_1] [weight_1]

[value_2] [weight_2]

...

For example, the third line of the file is "50074 834558", indicating that the second item has value 50074 and size 834558, respectively. As before, you should assume that item weights and the knapsack capacity are integers.

This instance is so big that the straightforward iterative implemetation uses an infeasible amount of time and space. So you will have to be creative to compute an optimal solution. One idea is to go back to a recursive implementation, solving subproblems --- and, of course, caching the results to avoid redundant work --- only on an "as needed" basis. Also, be sure to think about appropriate data structures for storing and looking up solutions to subproblems.

In the box below, type in the value of the optimal solution.

ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!

'''


import numpy as np
import knapsack_cython as knc
import sys


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


def read_items(fname, nlines=None):
    data = np.loadtxt(fname)
    W = int(data[0, 0])
    n = int(data[0, 1])
    data = data[1:, :]
    items = {}
    if (nlines is None):
        nlines = n
    for i in xrange(1, nlines + 1):
        items[i] = {"weight": data[i - 1, 1],
                    "value": data[i - 1, 0]}

    return W, items


def find_nitems_better(items):
    n = len(items)
    # Number of elements the item i is striclty better than
    counts = []
    for i in xrange(1, n + 1):
        counts.append((i, sum([is_better(items[i], items[j])
                               for j in xrange(i + 1, n)])))
    # Sorted
    counts = sorted(counts, key=lambda x: x[1], reverse=True)
    return counts


def find_smallestset_gooditems(items, counts, W):
    # Find the smallest set of good items that exceed the maximum weight W
    s = 0
    i = 1
    while (s <= W):
        s += items[counts[i][0]]["weight"]
        i += 1
    golden_items = [x[0] for x in counts[0:i]]
    return golden_items


def exclude_items(items, golden_items):
    # For each item, check if it is strictly worse than
    # ALL elements in golden_items
    # If it is worse, then exclude it from the analysis
    n = len(items)
    for i in xrange(1, n):
        if all([is_worse(items[i], items[gold]) for gold in golden_items]):
            items.pop(i)

    return items


def main(args):
    fname = "knapsack_big.txt"
    if (len(args) == 3):
        nlines = int(args[1])
        W = int(args[2])
    else:
        nlines = None
        W = None
    if W:
        _, items = read_items(fname, nlines=nlines)
    else:
        W, items = read_items(fname, nlines=nlines)

    counts = find_nitems_better(items)

    golden_items = find_smallestset_gooditems(items, counts, W)

    print "item length = ", len(items)
    items = exclude_items(items, golden_items)

    print "New item length = ", len(items)
    values = np.array([x["value"] for x in items.values()])
    weights = np.array([x["weight"] for x in items.values()])

    sol = knc.knapsack(W, values, weights)
    print "sol: ", sol


if __name__ == "__main__":
    main(sys.argv)

# Run the algorithm on the subset of items
#n = len(items)
#previous = np.zeros((W+1,))
#current = np.zeros((W+1,))
#
#
#solution = [0]
# for (i,item) in items.iteritems():
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
# print S
