array = [1,3,4,5,2,11,12]

def bubble_sort(array):
    n = len(array)

    for i in range(n):

        #base case - terminates array if nothing left to sort
        already_sorted = True

        #look at each item one by one and compare with adjacent item
        for j in range(n - i - 1):
            if array[j] > array[j+1]:
                #swap 
                array[j], array[j+1] = array[j+1], array[j]

                #flag false
                already_sorted = False 

        if already_sorted:
            break

    return array 
    