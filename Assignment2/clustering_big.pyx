'''
In this question your task is again to run the clustering algorithm from lecture, but on a MUCH bigger graph. So big, in fact, that the distances (i.e., edge costs) are only defined implicitly, rather than being provided as an explicit list.

The data set is below.

clustering_big.txt
The format is:

[# of nodes] [# of bits for each node's label]

[first bit of node 1] ... [last bit of node 1]

[first bit of node 2] ... [last bit of node 2]

...

For example, the third line of the file "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" denotes the 24 bits associated with node #2.

The distance between two nodes u and v in this problem is defined as the Hamming distance--- the number of differing bits --- between the two nodes' labels. For example, the Hamming distance between the 24-bit label of node #2 above and the label "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3 (since they differ in the 3rd, 7th, and 21st bits).

The question is: what is the largest value of k such that there is a k-clustering with spacing at least 3? That is, how many clusters are needed to ensure that no pair of nodes with all but 2 bits in common get split into different clusters?

NOTE: The graph implicitly defined by the data file is so big that you probably can't write it out explicitly, let alone sort the edges by cost. So you will have to be a little creative to complete this part of the question. For example, is there some way you can identify the smallest distances without explicitly looking at every pair of nodes?


'''

from itertools import izip, imap
from itertools import permutations
import operator
import UnionFind


cpdef aux_permutations(l):
    initial = '0'*l
    out = []
    for i in xrange(0,l):
        z = list(initial)
        z[i] = '1'
        out.append(int(''.join(z), 2))
        for j in xrange(i+1, l):
            w = list(z)
            w[j] = '1'
            out.append(int(''.join(w), 2))
    return out



cpdef hamming(str1, str2):
    assert len(str1) == len(str2)
    #ne = str.__ne__  ## this is surprisingly slow
    ne = operator.ne
    return sum(imap(ne, str1, str2))


cpdef invert(bit):
    if bit != '0' and bit != '1':
        raise ValueError
    return '1' if bit == '0' else '0'


cpdef similar(v):
    out = []
    for i in range(len(v)):
        out.append(v[:i] + invert(v[i]) + v[i + 1:])
        for j in range(i + 1, len(v)):
            out.append(v[:i] + invert(v[i]) + v[i + 1:j] +
                       invert(v[j]) + v[j + 1:])
    return out


cpdef similar2(v, aux_permut, l):
    return ['{0:0{1}b}'.format(v ^ w,l) for w in aux_permut]


cpdef find_clusters(fname, n):
    cdef vertices = ["".join(x.split(' ')) for x in open(
        fname, 'r').read().split('\n')[0:n]]

    #aux_perm = aux_permutations(24)
    
    nodes = {}
    for (i,v) in enumerate(vertices):
        nodes[v] = i
    # Now the number of clusters if the same as the number of nodes
    cdef int clusters = len(nodes)
    U = UnionFind.UnionFind(len(vertices))

    # For each vertex..
    for v in vertices:
        # Check if the node exists
        try:
            node = nodes[v]
        except:
            continue

        # If it does, find the similar nodes (hamming distance <= 2)
        
        #s = int(v, 2)
        #sim = similar2(s, aux_perm, 24)
        sim = similar(v)
        # For each similar node, if it is in the graph and no loops are created, assign it 
        # to the same cluster as v, and decrease the number of clusters.
        for friend in sim:
            if nodes.get(friend):
                    n1 = node - 1
                    n2 = nodes[friend] - 1
                    #print n1, n2
                    #print U.size
                    if (U.find(n1) != U.find(n2)):
                        U.union(n1, n2)
                        clusters -= 1
    

    print "N clusters: ", clusters


