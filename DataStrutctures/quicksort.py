# Python program to implement Quick Sort

# Partition method takes element as pivot
# places the pivot element at its correct position
# in sorted array, and places al smaller (smaller than pivot)
# to left of pivot and all greater elements of right pivot

def partition(arr,start,end):
    pivot = arr[start]    # pivot to first array element
    low = start + 1       # initial index
    high = end            # last index

    while True:
        # If the current value we are looking at is larger than the pivot
        # it's the right place (right side of the pivot) and we can move left
        # to the next element
        # We also need to make sure we haven't surpassed the low pointer, since that indicates
        # we have already moved all the elements to their correct side of the pivot
        while low <= high and arr[high] >= pivot:
            high = high - 1

        # Opposite process to the one above
        while low <= high and arr[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            arr[low],arr[high] = arr[high],arr[low]
            # loops continues
        else:
            # We exit out of loop
            break

    arr[start],arr[high] = arr[high],arr[start]

    return high
        


# The main function implements QuickSort
# arr[] -> array to be sorted
# start -> starting index
# end -> ending index

# Function to do quick sort
def quickSort(arr,start,end):
    if start > end:
        return

    p = partition(arr,start,end)
    quickSort(arr,start,p-1)
    quickSort(arr,p+1,end)

if __name__ == '__main__':
    arr = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
    quickSort(arr,0,len(arr)-1)
    
    print (arr)