"""Branch and bound approximation for vertex set cover problem"""

if __name__ == '__main__':
    f = open('offline_4_input.txt')
    line = f.readline()
    l = line.rstrip().split(" ")
    n = l[0]
    m = int(l[1])
    # print(n ,m)
    # print(line)

    for line in f :
        l = line.rstrip().split(" ")
        print(l)
