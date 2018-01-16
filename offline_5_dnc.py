import random
import resource, sys

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

def partition(array, low, high):
    """Hoare Partition scheme

    :array: TODO
    :low: TODO
    :high: TODO
    :returns: TODO

    """
    pivot = array[low]
    i = low + 1
    j = high

    done = False
    
    while not done:
        print(array)
        while (i<=j and array[i]<=pivot):
            j = j - 1
        while(array[j]>pivot and j>=i):
            j = j-1
        if (j<i):
            done=True
        else:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp

        temp = array[low]
        array[low] = array[j]
        array[j] = temp 

        return j

def findquicksort(array, high):
    print(array)
    array = quicksort(array, 0, high)

def quicksort(array, low, high):
    """TODO: Docstring for quicksort.
    Taken from Cormen/Wikipedia

    :array: unsorted list
    :low: TODO
    :high: TODO
    :returns: TODO

    """
    print(array, low, high)
    if low<high :
        p = partition(array, low, high)
        array = quicksort(array, low, high-1)
        array = quicksort(array, p+1, high)
    print(array)

    # return array
   

if __name__ == '__main__':
    resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
    sys.setrecursionlimit(10**6) 

    f = open('offline_5_input.txt')
    num_of_tests = int(f.readline())
    for _ in range(num_of_tests):
        n = int(f.readline())
        line = f.readline().rstrip().split(" ")
        array = []
        for i in line:
            array.append(int(i))
        print(array)
        # median = rand_median(array)
        # median = median[0]

        # print(median)
        # median = 9
        # res_arr = findquicksort(array, median)
        findquicksort(array, len(array)-1)
        print(array)

