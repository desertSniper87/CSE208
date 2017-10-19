from collections import defaultdict

import sys


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
    # f = open('offline_2_input_2.txt')

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

        # print(graph)
        print("Source?")
        source = int(input())
        bellman_ford(graph, source, num_of_vert, num_of_edge)

        num_of_tests = num_of_tests - 1

    print("End of program")

    
