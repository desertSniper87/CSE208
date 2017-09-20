from collections import defaultdict

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

    print(graph)
