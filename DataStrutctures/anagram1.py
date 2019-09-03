### Programa de Anagrama en python

def is_anagram(str1, str2):
    list_str1 = list(str1)
    list_str1.sort()
    list_str2 = list(str2)
    list_str2.sort()

    return (list_str1 == list_str2)


def contador (str):
    """
    La funcion contador lanza el conteo de la cadena a introducir
    """
    cont = 0
    for letra in str:
        cont = cont + 1
    
    return (cont)

print("La palabra introducida tiene " + str(contador('paso')) + " letras")
print(is_anagram('paso','sopa'))
print(is_anagram('top','pat'))