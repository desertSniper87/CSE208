from collections import defaultdict

import sys


def prim(graph):
    mst = defaultdict(dict)
    weights = {}

    for i in graph:
        mst[i] = []

        # if ( graph[i]!={} ):
        # min_weight = sys.maxsize
        # min_key = 0

        # for key in graph[i]:
        # if graph[i][key]<min_weight:
        # min_weight = graph[i][key]
        # min_key = key
        # mst[i].append(min_key)
        # weights[i, min_key] = min_weight
        # # visited.append(i)

        # enqueue edges connected to s in PQ (by inc weight)
        # while (!PQ.isEmpty)
        #   if (vertex v linked with e = PQ.remove ∉ T)
        #       T = T ∪ {v, e}, enqueue edges connected to v
        # else ignore e

    source = 1
    front = []
    visited = []

    front.append(source)
    while(front):
        min_weight = sys.maxsize
        for n in front:
            for key in graph[n]:
                if graph[n][key] < min_weight and key not in visited:
                    min_weight = graph[n][key]
                    min_key = key
                    min_n = n
        if min_key not in visited:
            front.append(min_key)
            mst[min_n].append(min_key)
            weights[min_n, min_key] = min_weight
            visited.append(min_key)
        if n not in visited:
            visited.append(n)

        for y in front:
            x = [x for x in graph[y]]
            if set(visited) > set(x):
                front.remove(y)
            # print("n: ",n , "y: ", y,  "x:", x, "visited", visited)
            # print("front:", front)
            # if not x:
                # min_weight = sys.maxsize
                # for i in graph:
                # if n in graph[i]:
                # if graph[i][n] < min_weight:
                # key = i
                # min_weight = graph[i][n]
                # if (key not in visited and min_weight!=sys.maxsize):
                # mst[key].append(i)
                # weights[key, i] = min_weight
                # front.remove(n)
            # elif set(visited)>set(x):

    return mst, weights

def bellman_ford(graph, source, num_of_vert, num_of_edge):
    inf = float("inf")
    d = {}
    pi = {}
    for v in graph:
        d[v] = inf
        pi[v] = None
    d[source] = 0

    for _ in range(num_of_vert-2):
        for u in graph:
            for v in graph[u]:
                # relax(u, v, graph[u][v])
                if d[v] > d[u] + graph[u][v]:
                    d[v] = d[u] + graph[u][v]
                    pi[v] = u

    print(d)
    print(pi)

    for u in graph:
        for v in graph[u]:
            if d[v] >  d[u] + graph[u][v]:
                return False

    return True





        





if __name__ == '__main__':
    f = open('offline_2_input.txt')

    num_of_tests = int(f.readline())

    while(num_of_tests):
        num_of_vert = int(f.readline())
        num_of_edge = int(f.readline())

        graph = defaultdict(dict)
        for i in range(1, num_of_vert + 1):
            graph[i] = {}

        for _ in range(0, num_of_edge):
            line = f.readline().rstrip().split(" ")
            graph[int(line[0])][int(line[1])] = float(line[2])
            graph[int(line[1])][int(line[0])] = float(line[2])

        # print(graph)
        print("Source?")
        source = int(input())
        bellman_ford(graph, source, num_of_vert, num_of_edge)

        num_of_tests = num_of_tests - 1

    print("End of program")

    
