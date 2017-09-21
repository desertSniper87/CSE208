from collections import defaultdict

import sys


def prim(graph):
    mst = defaultdict(dict)
    weights = {}
    for i in graph:
        mst[i] = []
        if (graph[i]!={}):
            min_weight = sys.maxsize
            min_key = 0
            for key in graph[i]:
                if graph[i][key]<min_weight:
                    min_weight = graph[i][key]
                    min_key = key
            mst[i].append(min_key)
            weights[i, min_key] = min_weight
    return mst




if __name__ == '__main__':
    f = open('input_offline_1.txt')

    num_of_vert = int(f.readline())
    num_of_edge = int(f.readline())

    graph = defaultdict(dict)
    for i in range(1, num_of_vert+1):
        graph[i] = {}


    for _ in range(0, num_of_edge):
        line = f.readline().rstrip().split(" ")
        graph[int(line[0])][int(line[1])] = int(line[2])

    mst = prim(graph)
    print(mst)
