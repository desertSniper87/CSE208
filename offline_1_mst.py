from collections import defaultdict

import sys

if __name__ == '__main__':
    f = open('input_offline_1.txt')

    parts = f.readline().rstrip().split(" ")
    if "" in parts:
        parts.remove("")
    print(parts)
    num_of_vert, num_of_edge = int(parts[0]), int(parts[1])

    graph = defaultdict(list)
    for i in range(1,num_of_t+1):
        graph[i] = []

    # print(graph)
    for i in range (0, num_of_edge):
        line = input().rstrip().split(" ")
        # line = f.readline().rstrip().split(" ")
        if "" in line:
            line.remove("")
        # print(line)
        graph[int(line[0])].append(int(line[1]))
        # print(graph)





