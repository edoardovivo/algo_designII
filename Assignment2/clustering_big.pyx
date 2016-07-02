import csv
import numpy as np
import UnionFind


def invert(bit):
    if bit != '0' and bit != '1':
        raise ValueError
    return '1' if bit == '0' else '0'


def similar(v):
    out = []
    for i in range(len(v)):
        out.append(v[:i]+invert(v[i]) + v[i+1:])
        for j in range(i+1, len(v)):
            out.append(v[:i]+invert(v[i])+v[i+1:j]+invert(v[j])+v[j+1:])
    return out


def main2():
    vertices = ["".join(x.split(' ')) for x in open('clustering_big.txt', 'r').read().split('\n')[0:-1]]
    heads = {}
    for v in vertices:
        heads[v] = v
    clusters = len(heads) 

    cnt = 0
    for v in vertices:
        cnt +=1 
        print cnt
        v_head = heads[v]
        while heads[v_head] != v_head:
            v_head = heads[v_head]

        for friend in similar(v):
            if heads.get(friend):
                #print "inside"
                #heads[v_head].append(friend)
                #heads.pop(friend, None)
                head = heads[friend]
                while heads[head] != head:
                    head = heads[head]
                if v_head != head:
                    heads[head] = v_head
                    clusters -= 1
    print clusters