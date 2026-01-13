class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]  # 记忆化数组
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(x, y):
            if dp[x][y] != 0:
                return dp[x][y]
            
            max_len = 1  # 至少包含自己
            
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                
                # 越界检查
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                
                # 递增条件
                if matrix[nx][ny] > matrix[x][y]:
                    length = 1 + dfs(nx, ny)
                    max_len = max(max_len, length)
            
            dp[x][y] = max_len
            return max_len
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        
        return res
