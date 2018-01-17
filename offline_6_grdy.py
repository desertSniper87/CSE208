import queue


class Node:
    def __init__(self, cargo, left=None, right=None):

        self.cargo = cargo
        self.left  = left
        self.right = right

    def __str__(self):
        return str(cargo)

def traverse(node, value):
    if value< node.cargo:
        traverse(node.left, value)
    else:
        traverse(node.right, value)


if __name__ == '__main__':
    f = open('offline_6_input.txt')
    num_of_tests = int(f.readline())
    for _ in range(num_of_tests):
        n = int(f.readline())
        freq_dic = {}
        freq_q = queue.PriorityQueue()
        for i in range(n):
            line = f.readline().rstrip().split(" ")
            freq_dic[line[0]] = int(line[1])
            freq_q.put((int(line[1]), line[0])) 
        
        # print(freq_q.queue)
        while(freq_q.qsize()>1):
            left = freq_q.get()
            right = freq_q.get()
            node = Node(left[0]+right[0], left, right)
            freq_q.put((left[0]+right[0], node))

        root = freq_q.get()


        print(freq_dic)
        for key, value in sorted(freq_dic, key=freq_dic.get, reverse=False):
            traverse(root, value)

            
        
            

