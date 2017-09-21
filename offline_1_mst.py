from collections import defaultdict

import sys


def prim(graph):
    # print(graph)
    mst = defaultdict(dict)
    weights = {}
    # source = 1
    # mst[source] = []
    # neighbors = []
    for i in graph:
        mst[i] = []
        if (graph[i]!={}):
            # print(graph[i])
            min_weight = sys.maxsize
            min_key = 0
            for key in graph[i]:
                # print(graph[i][key])
                if graph[i][key]<min_weight:
                    min_weight = graph[i][key]
                    min_key = key
                # for val in graph[i][key]:
                    # print(val)
                    # if graph[i][key] < min_weight:
                        # min_weight = graph[i][key]
                        # print (graph[i])
                        # print (graph[i][key])
            # print(min_weight)
            # print(min_key)
            mst[i].append(min_key)
            weights[i, min_key] = min_weight
            # print(mst)
            # print(weights)
    return mst


    # for


if __name__ == '__main__':
    f = open('input_offline_1.txt')

    num_of_vert = int(f.readline())
    num_of_edge = int(f.readline())

    graph = defaultdict(dict)
    for i in range(1, num_of_vert+1):
        graph[i] = {}

    # print(graph)
    # for i in range(0, num_of_edge):
    # line = input().rstrip().split(" ")
    # line = f.readline().rstrip().split(" ")
    # print(line)
    # if "" in line:
    # line.remove("")
    # print(line)
    # graph[int(line[0])].append(int(line[1]))
    # print(graph)

    for _ in range(0, num_of_edge):
        line = f.readline().rstrip().split(" ")
        # print(line)
        graph[int(line[0])][int(line[1])] = int(line[2])
        # print(graph)

    mst = prim(graph)
    print(mst)

    # print(graph)
