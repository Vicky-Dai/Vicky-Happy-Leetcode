class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid) #行数 因为 [[0,0],[1,0]]
        n = len(obstacleGrid) #列

        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
            return 0 #如果起始位置有障碍，直接没法走
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 0:  
                dp[i][0] = 1
            else:
                break #遇到障碍物，直接退出循环，后面默认都是0
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]