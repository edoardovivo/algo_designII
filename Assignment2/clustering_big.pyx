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


cpdef find_clusters(fname):
    vertices = ["".join(x.split(' ')) for x in open(
        fname, 'r').read().split('\n')[0:10]]
    nodes = {}
    # This gives u a dictionary where both key and values are
    # given by the same string 
    for v in vertices:
        nodes[v] = v
    # Now the number of clusters if the same as the number of nodes
    clusters = len(nodes)

    #cnt = 0
    # For each vertex..
    for v in vertices:
        #cnt += 1
        #print cnt
        # Get the value for the vertex
        v_head = nodes[v]
        # If key and value are different
        # then v_head is equal to the VALUE
        while nodes[v_head] != v_head:
            v_head = nodes[v_head]

        # sim is the set of all nodes at distance at most 2 from v
        sim = similar(v)
        for friend in sim:
            # If the friend node is in the graph
            if nodes.get(friend):
                # Consider the value associated with that node
                head = nodes[friend]
                # Consider the value associated with the key head
                # If head and its value are different, then reassign 
                # head as its correct value
                while nodes[head] != head:
                    head = nodes[head]
                # Compare v_head and head
                # If they are different, they belong to the 
                # same cluster (?)
                if v_head != head:
                    nodes[head] = v_head
                    clusters -= 1
    print nodes
    print "N clusters: ", clusters


cpdef find_clusters2(fname):
    vertices = ["".join(x.split(' ')) for x in open(
        fname, 'r').read().split('\n')[0:200]]
    nodes = {}
    for (i,v) in enumerate(vertices):
        nodes[v] = i
    # Now the number of clusters if the same as the number of nodes
    clusters = len(nodes)
    #cnt = 0
    # For each vertex..
    for v in vertices:
        try:
            node = nodes[v]
        except:
            continue
        sim = similar(v)
        for friend in sim:
            if nodes.get(friend):
                    nodes.pop(friend) #nodes[friend] = node
                    clusters -= 1
        nodes.pop(v)
        #cnt += 1
        #print cnt
        # Get the value for the vertex
        #v_head = nodes[v]
        ## If key and value are different
        ## then v_head is equal to the VALUE
        #while nodes[v_head] != v_head:
        #    v_head = nodes[v_head]
#
#        ## sim is the set of all nodes at distance at most 2 from v
#        #sim = similar(v)
#        #for friend in sim:
#        #    # If the friend node is in the graph
#        #    if nodes.get(friend):
#        #        # Consider the value associated with that node
#        #        head = nodes[friend]
#        #        # Consider the value associated with the key head
#        #        # If head and its value are different, then reassign 
#        #        # head as its correct value
#        #        while nodes[head] != head:
#        #            head = nodes[head]
#        #        # Compare v_head and head
#        #        # If they are different, they belong to the 
#        #        # same cluster (?)
#        #        if v_head != head:
#        #            nodes[head] = v_head
        #            clusters -= 1
    print "N clusters: ", clusters


