test = [5, 2, 3, 4, 7, 1]

def selection_sort( arr ):
    print(f'starting array: {arr} \n')
    for i in range(0, len(arr)-1):
        current_index = i
        smallest_index = current_index
        for j in range(current_index, len(arr)):
            if arr[j] < arr[current_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    print(f'ending array: {arr} \n')
    return arr

def bubble_sort( arr ):
    # loop through the array once for each element 
    for i in range(0, len(arr) - 1):
        # find smallest element in array 
        for i in range(0, len(arr)-1):
            # if current element is bigger than one to
            #the right of it:
            if arr[i] > arr[i+1]:
                # swap smaller element to the left
                arr[i], arr[i+1] = arr[i+1], arr[i]
                print(arr)
    return arr

bubble_sort(test)
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr