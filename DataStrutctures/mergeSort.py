# Python implementation  for the Merge Sort algorithm

def mergeSort(arr):
    n = len(arr)
    mid = n // 2

    if n > 1:
        l = arr[:mid]
        r = arr[mid:]

        mergeSort(l)
        mergeSort(r)

        i,j,k=0,0,0

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                arr[k] = l[i]
                i=i+1
            else:
                arr[k] = r[j]
                j=j+1

            k=k+1
        
        while i < len(l):
            arr[k] = l[i]
            i=i+1
            k=k+1

        while j < len(r):
            arr[k] = r[j]
            j=j+1
            k=k+1

    print ("Merging ",arr)

if __name__ == '__main__':
    arr = [54,26,93,17,77,31,44,55,20]
    mergeSort(arr)
    print(arr)



