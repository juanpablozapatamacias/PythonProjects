from clasePila import Pila

def calculadora_polaca(elementos):
    """ Dada una lista de elementos que representan las componentes de una expresion de una notacion polaca
        inversa, evalua dicha expresion. Si la expresion esta mal formada, levanta un value error
    """

    p = Pila()
    for elemento in range(len(elementos)):
        print ("DEBUG: ",elemento)

        #Intenta convertirlo a numero
        try:
            numero = float(elemento)
            p.apilar(numero)
            print("DEBUG: apila", numero)

        except ValueError:
            # Si no es un operando válido, levanta ValueError
            if elemento not in "+-*/ %" or len(elemento) != 1:
                raise ValueError("Operando inválido")
            # Si es un operando válido, intenta desapilar y operar
            try:
                a1 = p.desapilar()
                print ("DEBUG: desapila ",a1)
                a2 = p.desapilar()
                print ("DEBUG: desapila ",a2)
            # Si hubo problemas al desapilar
            except ValueError:
                print ("DEBUG: error pila faltan operandos")
                raise ValueError("Faltan operandos")

            if elemento == "+":
                resultado = a2 + a1
            elif elemento == "-":
                resultado = a2 - a1
            elif elemento == "*":
                resultado = a2 * a1
            elif elemento == "/":
                resultado = a2 / a1
            elif elemento == " %":
                resultado = a2 % a1
            print ("DEBUG: apila ", resultado)
            p.apilar(resultado)
        # Al final, el resultado debe ser lo único en la Pila
        res = p.desapilar()
        if p.esVacia():
            return res
        else:
            print ("DEBUG: error pila sobran operandos")
            raise ValueError("Sobran operandos")

if __name__ == '__main__':
    calculadora_polaca("5+((1+2)*4)-3")

            
