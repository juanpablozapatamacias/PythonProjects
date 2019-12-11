# Python program to implement Binary Search

def binarySearch(A, target):
    start,end,pivot,i = 0,len(A),0,0

    target = int(target)

    while start <= end:
        pivot = int(start + (end - start) / 2)

        if A[pivot] == target:
            return pivot
        
        if A[pivot] < target:
            start = pivot + 1

        if A[pivot] > target:
            end = pivot - 1

    return -1

if __name__ == '__main__':
    arr = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
    arr.sort()

    print(arr)
    val = input()
    src = binarySearch(arr,val)

    if src != -1:
        print("The element ", val, " is located at index ",src)
    else:
        print("Element not found")

