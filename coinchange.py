# Dynamic programming Python implementation of coin
def count(S,m,n):
    # S = array of supply valued coins
    # m = len of S
    # n = Value fo cents
    table = [[0 for x in range(m)] for x in range(n+1)]

    # fill the entries for 0 value case
    for i in range(m):
        table[0][i] = 1

    # Fill the rest of tbale entries in bottom up matter
    for i in range(1, n+1):
        for j in range(m):
            # count of solutions including S[j]
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0

            # Count of solution excluding S[j]
            y = table[i][j-1] if j >= 1 else 0

            # Total count 
            table[i][j] = x + y

    return table[n][m-1]

arr = [2,5,3,6]
m = len(arr)
n = 10
print (count(arr,m,n))