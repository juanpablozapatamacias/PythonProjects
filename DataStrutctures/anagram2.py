### Programa de anagrama 2s

def is_anagram(str1,str2):
    alist1 = list(str1)
    alist2 = list(str2)

    ### alist1.sort()
    ### alist2.sort()

    l1 = ordenaChar(alist1)
    l2 = ordenaChar(alist2)

    pos = 0
    matches = True

    while pos < len(str1) and matches:
        if l1[pos] == l2[pos]:
            pos = pos + 1
        else:
            matches = False
    
    return (matches)

def ordenaChar(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]:
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp
    
    return(lista)

print (is_anagram('sopa','paso'))