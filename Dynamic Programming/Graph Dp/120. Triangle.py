class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        # 定义：走到第 i 行第 j 个元素的最小路径和是 dp[i][j]
        dp = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            # 因为求最小值，所以全都初始化为极大值
            dp[i] = [float('inf')] * n
        # base case
        dp[0][0] = triangle[0][0]
        # 进行状态转移
        for i in range(1, n):
            row = triangle[i]
            for j in range(len(row)):
                # 状态转移方程
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + row[j]
                else:
                    dp[i][j] = dp[i - 1][j] + row[j]
        # 找出落到最后一层的最小路径和
        res = float('inf')
        for j in range(n):
            res = min(res, dp[n - 1][j])
        
        return res