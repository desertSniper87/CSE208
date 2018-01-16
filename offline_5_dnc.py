import random

def rand_median(array):
    """ Dasgupta et al page 57 """

    l = len(array) 
    median = []
    rand_array = random.sample(array, l)
    # print(rand_array)
    for i in rand_array:
        selection_l = []
        selection_h = []
        for x in array:
            if (i<x):
                selection_l.append(x)
            elif(i>x):
                selection_h.append(x)

        a = len(selection_l)
        b = len(selection_h)
        if( a==b or a==b-1 or a==b+1 ):
            median.append(i)
    
    return median


   

if __name__ == '__main__':
    f = open('offline_5_input.txt')
    num_of_tests = int(f.readline())
    for _ in range(num_of_tests):
        n = int(f.readline())
        line = f.readline().rstrip().split(" ")
        array = []
        for i in line:
            array.append(int(i))
        # print(array)
        median = rand_median(array)
        print(median)

    # while (num_of_tests):
        # match    = int(line[2])
        # mismatch = int(line[3])
        # gap      = int(line[4])
        # seq1     = f.readline().rstrip()
        # seq2     = f.readline().rstrip()

        # rows = len(seq1) + 1
        # cols = len(seq2) + 1

        # score_matrix, start_pos = create_score_matrix(rows, cols)

        # seq1_aligned, seq2_aligned = traceback(score_matrix, start_pos)

        # alignment_str, idents, gaps, mismatches = alignment_string(seq1_aligned, seq2_aligned)
        # alength = len(seq1_aligned)
        # print_matrix(score_matrix)
        # print()
        # print(seq1_aligned)
        # print(alignment_str)
        # print(seq2_aligned)
        # print()


        # num_of_tests = num_of_tests - 1
