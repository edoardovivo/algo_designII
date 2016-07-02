'''
In this programming problem and the next you'll code up the knapsack algorithm from lecture.

Let's start with a warm-up. Download the text file below.

knapsack1.txt
This file describes a knapsack instance, and it has the following format:

[knapsack_size][number_of_items]

[value_1] [weight_1]

[value_2] [weight_2]

...

For example, the third line of the file is "50074 659", indicating that the second item has value 50074 and size 659, respectively.

You can assume that all numbers are positive. You should assume that item weights and the knapsack capacity are integers.

In the box below, type in the value of the optimal solution.

ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!
'''


import numpy as np


def read_items(fname, nlines=None):
    data = np.loadtxt(fname)
    W = int(data[0, 0])
    n = int(data[0, 1])
    data = data[1:, :]
    items = {}
    if (nlines is None):
        nlines = n
    for i in xrange(1, nlines):
        items[i] = {"weight": data[i - 1, 1],
                    "value": data[i - 1, 0]}

    return W, items


def main():
    fname = "knapsack1.txt"
    W, items = read_items(fname)
    n = len(items)
    # Solution
    A = np.zeros((n, W + 1), dtype=float)

    for i in xrange(1, n):
        for x in xrange(0, W + 1):
            ind_weight = x - items[i + 1]["weight"]
            if (ind_weight >= 0):
                A[i, x] = max(A[i - 1, x], A[i - 1, ind_weight] +
                              items[i + 1]["value"])
            else:
                A[i, x] = A[i - 1, x]

    S = A[n - 1, W]
    print "S: ", S

if __name__ == "__main__":
    main()
