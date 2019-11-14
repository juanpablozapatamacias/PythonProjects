class Islas:

    def __init__(self,arr):
        self.arr = arr

    def setArr(self,arr):
        self.arr = arr

    def getArr(self):
        return self.arr

    def numIslas(self,arr):
        total = 0
        nRows = len(arr)
        nCols = len(arr[0])

        visited = [[False for j in range(nCols)]for i in range(nRows)]

        for i in range(nRows):
            for j in range(nCols):
                if arr[i][j] ==1 and visited[i][j] == False:
                    self.__findIslas__(arr,visited,i,j)
                    total +=1

        return total

    def __findIslas__(self,arr,visited,a,b):
        if arr[a][b]==1 and visited[a][b] == False:
            visited[a][b] = True
            '''

            #south
            if a < (len(arr) - 1):
                self.__findIslas__(arr,visited,a+1,b)

            #east
            if b < (len(arr) - 1):
                self.__findIslas__(arr,visited,a,b+1)

            #north
            if a >= 1:
                self.__findIslas__(arr,visited,a-1,b)
            
            #west
            if b >= 1:
                self.__findIslas__(arr,visited,a,b-1)
            '''

            if a != 0:
                self.__findIslas__(arr,visited,a-1,b)

            if a != len(arr) - 1:
                self.__findIslas__(arr,visited,a+1,b)

            if b != 0:
                self.__findIslas__(arr,visited,a,b-1)

            if b != len(arr[0]) - 1:
                self.__findIslas__(arr,visited,a,b+1)

A = [[0,1,1,0,1],
     [0,1,0,0,1],
     [1,0,1,1,1]]

miIslita = Islas(A)

print(miIslita.numIslas(miIslita.getArr()))
            

