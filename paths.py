def numberOfPaths(m,n):
    dp = [1 for i in range(n)]

    for i in range(m-1):
        for j in range(1,n):
            dp[j] += dp[j-1]

    return dp[n-1]

def numberOfPathsWithObstacles(arr):
    paths = [[0] * len(arr) for i in arr] #2d array initialize

    if arr[0][0] == 0: # initialize left corner
        paths[0][0] = 1

    for i in range(1, len(arr)): #initializae first column
        if arr[i][0] == 0:
            paths[i][0] = paths[i-1][0]
        
    for j in range(1, len(arr[0])): # initilize top row
        if arr[0][j] == 0:
            paths[0][j] = paths[0][j-1]

    for i in range(1,len(arr)):
        for j in range(1,len(arr[0])):
            if arr[i][j] == 0: #current cell without obstacle
                paths[i][j] = paths[i-1][j] + paths[i][j-1]

    return paths[-1][-1]
    
print("Find Paths with no obstacle,using coordinates")
print(numberOfPaths(2,3))
print(numberOfPaths(7,3))
print(numberOfPaths(4,5))

print("Find Paths with obstacle using 2d array")
A = [[0,0,0],[0,1,0],[0,0,0]]
print(numberOfPathsWithObstacles(A))