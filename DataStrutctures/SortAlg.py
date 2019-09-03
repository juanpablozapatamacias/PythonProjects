### Metodo ordenamiento burbuja

def ordenamientoBurbujaCorto(unaLista):
    intercambios = True
    numPasada = len(unaLista) - 1
    while numPasada > 0  and intercambios:
        intercambios = False
        for i in range(numPasada):
            if unaLista[i] > unaLista[i+1]:
                intercambios = True
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp
        
        print(unaLista) 
        numPasada = numPasada - 1

### Metodo ordenamiento Seleccion
def ordenamientoSeleccion(unaLista):
    for i in range(len(unaLista)):
        minimo = i
        for j in range(i,len(unaLista)):
            if unaLista[j] < unaLista[minimo]:
                minimo = j
        
        if minimo != i:
            aux = unaLista[i]
            unaLista[i] = unaLista[minimo]
            unaLista[minimo] = aux
        
        print(unaLista)

### Metodo ordenamiento Insercion
def ordenamientoInsercion(unaLista):
    for i in range(len(unaLista)):
        for j in range(i,0,-1):
            if unaLista[j-1] > unaLista[j]:
                aux = unaLista[j]
                unaLista[j] = unaLista[j-1]
                unaLista[j-1] = aux
        
        print (unaLista)

print("Ordenamiento Burbuja")
A = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
ordenamientoBurbujaCorto(A)
print()
print("Ordenamiento Seleccion")
B = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
ordenamientoSeleccion(B)
print()
print("Ordenamiento Insercion")
C = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
ordenamientoInsercion(C)
print()
### print (unaLista)