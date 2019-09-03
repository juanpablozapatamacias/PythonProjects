import random

digitos = (0,1,2,3,4,5,6,7,8,9)
codigo = ''

for i in range(4):
    candidato = random.choice(digitos)
    while candidato in digitos:
        candidato = random.choice(digitos)

    codigo = codigo + candidato

print ("Bienvenidos al mastermind")
print ("Adivina un numero de 4 cifras distintas")
propuesta = input("Que codigo propones? ")

intentos = 1

while propuesta != codigo:
    intentos = intentos + 1
    aciertos = 0
    coincidencias = 0

    for i in range(4):
        if propuesta[i] == codigo[i]:
            aciertos = aciertos + 1
        elif propuesta[i] in codigo:
            coincidencias = coincidencias + 1
    
    print ("Tu propuesta " + str(propuesta) + " tiene " + str(aciertos) \
        + " aciertos y " + str(coincidencias) + " coincidencias")
    
    propuesta = input("Que otro codigo propones? ")

print ("Felicidades!!!")