def suma(*args):
    print(args)
    return sum(args) * 0.05

def lista(*args):
    lst = []
    for item in args:
        lst.append(item)
    
    return lst

def bubbleSort(milista):
    intercambios = True
    numPasada = len(milista) - 1
    while numPasada > 0 and intercambios:
        intercambios = False
        for i in range(numPasada):
            if milista[i] > milista[i+1]:
                intercambios = True
                temp = milista[i]
                milista[i] = milista[i+1]
                milista[i+1] = temp
            
        print(milista)
        numPasada = numPasada - 1

print(suma(100,200,300,400,600,700))
### print(lista(100,200,300,80,90,1000))
bubbleSort(lista(5000,100,200,300,80,90,1000))