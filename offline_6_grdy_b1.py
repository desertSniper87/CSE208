

if __name__ == '__main__':
    f = open('offline_6_input.txt')
    num_of_tests = int(f.readline())
    for _ in range(num_of_tests):
        n = int(f.readline())
        freq_q = queue.PriorityQueue()
        for i in range(n):
            line = f.readline().rstrip().split(" ")
            freq_q.put((int(line[1]), line[0])) 
        
        while(freq_q.qsize()>1):
            left = freq_q.get()
            right = freq_q.get()
            node = Node(left, right)
            freq_q.put((left[0]+right[0], node))

        root = (freq_q.get())
        code_dic = traverse(root)

        for key in sorted(code_dic):
            print(key, code_dic[key])

            
        
            

