array = [1,4,2,3,9,5,6,7,10,8]

def insertion_sort(array):
    for i in range(1, len(array)):

        key_item = array[i]

        j = i-1

        while j >= 0 and array[j] > key_item:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = key_item 
    
    return array
