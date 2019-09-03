### Programa que crea una lista enlazada
import os

class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
    
    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,dato):
        self.dato=dato
    
    def asignarSiguiente(self,siguiente):
        self.siguiente = siguiente

class ListaNoOrdenada:
    def __init__(self):
        self.cabeza = None

    def estaVacia(self):
        return self.cabeza == None
    
    def agregar(self, item):
        temp = Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp
    
    def tamano(self):
        actual, contador = self.cabeza, 0
        
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()

        return contador
    
    def buscar(self, item):
        actual, encontrado = self.cabeza, False
        
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()
        
        return encontrado

    def remover(self, item):
        actual, previo, encontrado = self.cabeza, None, False
        
        while not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()

        if previo == None:
            self.cabeza = actual.obtenerSiguiente()
        else:
            previo.asignarSiguiente(actual.obtenerSiguiente)

    def imprimir(self):
        actual = self.cabeza

        while actual != None:
            print(actual.obtenerDato())
            actual = actual.obtenerSiguiente()

    def reverse(self):
        prev, curr, next = None, self.cabeza, None

        while curr is not None:
            next = curr.obtenerSiguiente()
            curr.asignarSiguiente(prev)
            prev = curr
            curr = next
        
        self.cabeza = prev

    def agregarValores(self, *args):
        for item in args:
            self.agregar(item)

    def agregarValListaEnlazada(self, lst):
        for i in range(len(lst)):
            self.agregar(lst[i])

def osclear():
    os.system('clear')

osclear()

milista = ListaNoOrdenada()
### milista.agregarValListaEnlazada(milista.agregarValores(100,200,300,80,90,900,1000))

milista.agregarValores(500,400,250,100,200,300,80,90,900,1000)
print ("Tamanio de la lista es igual a: " + str(milista.tamano()))
print ("Valores de la lista")
milista.imprimir()
print()
print ("Revertimos la lista e imprimimos de nuevo")
milista.reverse()
milista.imprimir()
print ("Realizar busqueda de elementos")
print (milista.buscar(90))
print (milista.buscar(1))
print ("Remover elementos de la lista")
milista.remover(100)
print (milista.tamano())