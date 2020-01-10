class Pila:
    """
    Representa una pila con operaciones de apilar, desapilar y verificar si esta vacia 
    """
    def __init__(self):
        """crear una pila vacia"""
        self.items=[]

    def apilar(self, x):
        """Agrega elemento x a la pila"""
        self.items.append(x)

    def desapilar(self):
        """Devuelve el elemento top y lo elimina de la pila"""
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("Pila Vacia")

    def esVacia(self):
        """Devuelve True si la lista esta vacia"""
        return self.items==[]

    def tamanyo(self):
        return len(self.items)

    def limpiar(self):
        return self.items.clear()

    

    