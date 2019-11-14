def copyArray(arr):
    copy = []

    for i in range(len(arr)):
        copy = appendToNew(copy,arr[i])

    return copy

def appendToNew(arr, value):
    bigger = []
    for i in range(len(arr)):
        bigger.append(arr[i])

    bigger.append(value)

    return bigger

def removeElement(arr,val):
    i,j=0,0
    while j < len(arr):
        if arr[j] != val:
            arr[i] = arr[j]
            i+=1
        
        j+=1
    
    return i

def imprimirListas(arr):
    for i in range(len(arr)):
        print (arr[i], end= " ")

def ejemploTupla():
    meses=("ENE","FEB","MAR","ABR","MAY","JUN","JUL","AGO","SEP","OCT","NOV","DIC")
    salir = False
    while(not salir):
        numero = int(input("Dame un Numero: "))
        if(numero == 0):
            salir = True
        else:
            if(numero >= 1 and numero <=len(meses)):
                print(meses[numero - 1])
            else:
                print("Inserta un numero entre 1 y ", len(meses))

def creaLista():
    lista = []
    salir = False
    while(not salir):
        numero = int(input("Dame un Numero: "))
        if(numero == 0):
            salir = True
        else:
            lista.append(numero)
    return lista

def findNonDuplicated(arr1, arr2):
    i,j,k=0,0,0

    while(i<len(arr1) and j<len(arr2)):
        if(arr1[i] < arr2[j]):
            print(arr1[i], end=" ")
            i+=1
            k+=1
        elif (arr2[j] < arr1[i]):
            print(arr2[j], end=" ")
            k+=1
            j+=1
        else:
            i+=1
            j+=1

    while(i<len(arr1)):
        print(arr1[i], end=" ")
        i+=1
        k+=1

    while(j<len(arr2)):
        print(arr2[j], end=" ")
        k+=1
        j+=1

def removeDuplicates(arr):
    if arr is None:
        return 0
    if (len(arr) <= 2):
        return len(arr)

    i,j=1,2

    arr.sort()

    while(j < len(arr)):
        if(arr[j] == arr[i] and arr[j] == arr[i-1]):
            j+=1
        else:
            i+=1
            arr[i] = arr[j]
            j+=1

    return i+1

def reverseArray(arr):
    b = [None]*len(arr)
    j = len(arr)

    for i in range(len(arr)):
        b[j-1] = arr[i]
        #b.append(arr[i])
        j-=1

    #b.reverse()        

    return b

def joinArrays(ar1, ar2):
    ar3 = [None]*(len(ar1) + len(ar2))
    m = len(ar1)
    n = len(ar2)

    ar1.sort()
    ar2.sort()

    count = 0

    for i in range(len(ar1)):
        ar3[i] = ar1[i]
        count+=1

    for j in range(len(ar2)):
        ar3[count] = ar2[j]
        count+=1

    return ar3

def findFirstAndLast(arr,target):
    res = [0,0]
    n = len(arr)
    first,last=-1,-1

    arr.sort()
    
    for i in range(n):
        if target != arr[i]:
            continue
        if(first == -1):
            first = i

        last = i

    res[0] = first
    res[1] = last

    return res

def countNegNumbersArray(ar):
    rows = len(ar)
    cols = len(ar[0])
    count = 0

    for i in range(rows):
        ar[i].sort()
        for j in range (cols):
            if ar[i][j] < 0:
                count += 1
            else:
                break

    print ("La cantidad de numeros negativos es ", count)

def searchRange(arr,target):
    res = []
    n = len(arr)
    first = -1
    last = -1

    for i in range(0,n):
        if (target != arr[i]):
            continue
        if (first == -1):
            first = i

        last = i

    res.append(first)
    res.append(last)

    return res

def missingNumber(nums):
    total = 0
    n=len(nums)

    for i in range(n):
        total += nums[i]

    return n*(n+1)/2-total



ar1 = [3,5,2,1,77,4,89,32,5,9,54,202,100,997,3,1,3,2,8,115,225,547]
ar2 = copyArray(ar1)

#print (ar2)
imprimirListas(ar2)

print ()

elements = removeElement(ar2,2)
print (elements)
imprimirListas(ar2)

ejemploTupla()

print()

l1 = []
l1 = creaLista()
l1.sort()
print(l1)

l1.sort(reverse=True)
print (l1)

print("Crear primera lista")
arre1=creaLista()
print("Crear segunda lista")
arre2=creaLista()
findNonDuplicated(arre1,arre2)

'''
arre3=[]
print ("Crear una nueva lista mas")
arre3 = creaLista()
print(removeDuplicates(arre3))
arre3 = reverseArray(arre3)
print (arre3)
'''
print(joinArrays(arre1,arre2))

arre5=[1,2,2,3,3,3,3,3,4,7,8,8,4]
print(findFirstAndLast(arre5,4))

A = [[3,-2,-1,1,2,6],
     [2,-2,0,1,4,6],
     [5,-9,1,2,3,4],
     [1,-10,-9,-8,-1,0],
     [5,2,4,-5,0,1]]

countNegNumbersArray(A)

B = [5,7,7,8,8,10]
print (searchRange(B,8))

print (missingNumber(B))

