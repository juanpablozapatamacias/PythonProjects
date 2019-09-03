### Imprime numeros pares 40 a 60
n = 40
h = ''
while n <= 60:
    if n%2 == 0:
        h+= " %i" %n

    n +=1

print (h)