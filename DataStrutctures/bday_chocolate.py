### Programa de Bday chocolate

def getWays(squares,d,m):
    ways=0
    sum=0

    if m <= len(squares):
        for i in range(m):
            sum = sum + squares[i]

    if sum == d:
        ways = ways + 1

    for j in range(len(squares) - m):
        sum = sum - squares[j] + squares [i+m]
        if sum == d:
            ways = ways + 1
    
    return ways

S = [1,1,1,1,1,1]
print(getWays(S,1,1))
