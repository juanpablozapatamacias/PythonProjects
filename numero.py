def divisibleSumPairs(n,k,arr):
    pairs = 0
    for i in range(n):
        for j in range(i+1,n):
            if (arr[i] + arr[j]) % k ==0:
                pairs += 1

    return pairs

def breakingScores(scores):
    max = scores[0]
    min= max
    cmax, cmin = 0,0

    for i in range(len(scores)):
        if scores[i] > max:
            max = scores[i]
            cmax +=1
        
        if scores[i] < min:
            min = scores[i]
            cmin +=1

    A = [cmax,cmin]
    return A



# Definimos un par de numeros uno flotante y otro entero
num1=int(6)
num2=float(2.5)
print(num1)
print(num2)

A=[1,3,2,6,1,2]
print (divisibleSumPairs(6,3,A))

B=[10,5,20,20,4,5,2,25,1]
print (breakingScores(B))

