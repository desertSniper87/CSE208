import queue


class Node:
    def __init__(self, cargo, left=None, right=None):

        self.cargo = cargo
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

def traverse(node, key, value, code=""):
    print(node)
    print(type(node))
    print(code)
    code = ""
    if (type(node)==tuple):
        print("test")
        if (node[1]==key):
            return code
        else:
            return
    elif value< node.cargo:
        code+("1")
        traverse(node.left, key, value)
    elif value> node.cargo:
        code+("0")
        traverse(node.right, key, value)
    return code


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
        
        while(freq_q.qsize()>1):
            left = freq_q.get()
            right = freq_q.get()
            node = Node(left[0]+right[0], left, right)
            freq_q.put((left[0]+right[0], node))

        root = (freq_q.get())[1]
        # print(root.cargo)


        # print(freq_dic)
        # for value in sorted(freq_dic, key=freq_dic.get, reverse=False):
        for key, value in freq_dic.items():
            traverse(root, key, value)

            
        
            

