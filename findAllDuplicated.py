def printDuplicated(arr):
    s  = dict()
    d = []

    for i in arr:
        if i not in s.keys():
            d.append(i)
            s[i] = 1

    print(d)


arr=[10,20,20,30,40,40,50,50]
printDuplicated(arr)