#from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # Если в начальной ячейке есть препятствие, то идти больше не куда
        if obstacleGrid[0][0] == 1:
            return 0

        # Количество путей для перехода в начальную точку = 1.
        obstacleGrid[0][0] = 1

        # Берутся значение из первой колонки и если текущее значение 0 а в предыдущем 1 то ставится 1, иначе 0. А если значением станет 0 то и все последующие значения будут 0.
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1) 

        # То же со строкой        
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                    # Суммируются возможные пути к точке
                else:
                    # В случае если там препятствия то возможных путей в эту точку будет 0
                    obstacleGrid[i][j] = 0

        # Возвращает количество путей из конечной точки            
        return obstacleGrid[m-1][n-1]
#print(Solution.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))