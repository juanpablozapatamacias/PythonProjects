class Tuplas:
    def __init__(self,tupla):
        self.tupla = tupla

    def setTupla(self, tupla):
        self.tupla = tupla

    def getTupla(self):
        return self.tupla

    '''
    Simulacion de operaciones con una tupla
    '''

    def ordena_tupla(self,t):
        lista =  list()
        for i in t:
            lista.append(i)

        lista.sort()
        t=tuple(lista)
        return t
    
    def inserta_elemento(self,t,e):
        lista = list(t)
        print ("Agregando valor a la tupla " + str(e))
        lista.append(e)
        t = tuple(lista)
        return t

    def remover_elemento(self,t,e):
        nueva = list()
        print ("Removiendo valor a la tupla " + str(e))
        for i in list(t):
            if not i == e:
                nueva.append(i)

        return tuple(nueva)

t = tuple()
t=(4,9,9,20,5,15)
print ("Original ", t)

miTupla = Tuplas(t)
t = miTupla.ordena_tupla(miTupla.getTupla())
print ("Tupla ordenada ", t)
print ("Insertar elemento a la tupla", miTupla.inserta_elemento(miTupla.getTupla(),7))
print ("Remover elemento de la tupla", miTupla.remover_elemento(miTupla.getTupla(),9))


