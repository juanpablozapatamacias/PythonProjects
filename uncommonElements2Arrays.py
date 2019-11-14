def printUncommon(arr1, arr2):

    i=j=k=0

    while(i < len(arr1) and j<len(arr2)):
        if(arr1[i] < arr2[j]):
            print(arr1[i], end=" ")
            i=i+1
            k=k+1
        elif (arr2[j] < arr1[i]):
            print(arr2[j], end=" ")
            k=k+1
            j=j+1
        else:
            i=i+1
            j=j+1

    while(i<len(arr1)):
        print(arr1[i], end=" ")
        i=i+1
        k=k+1

    while(j<len(arr2)):
        print(arr2[j], end=" ")
        j=j+1
        k=k+1

arr1=[1,4,3,2]
arr2=[1,2,2,3,3,3,3,3,4,7,8,8,4]

printUncommon(arr1,arr2)