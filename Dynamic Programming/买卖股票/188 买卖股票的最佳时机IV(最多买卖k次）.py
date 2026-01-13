#两次到4，k次就是2k个下表
#两个for 循环：i外层控制在第几天的price上，j内层控制第几次买卖
# 0 不操作 1 第一次持有 2 第一次不持有 3 第二次持有 4 第二次不持有 以此类推
class Solution:
    def maxProfit(self, k:int, prices:list[int]) -> int:
        if len(prices) == 0:
            return 0
        dp = [[0] * (2*k+1) for _ in range(len(prices))]
        for j in range(1, 2*k, 2):
            dp[0][j] = -prices[0]
        for i in range(1, len(prices)):
            for j in range(0, 2*k-1, 2):
                dp[i][j+1] = max(dp[i-1][j+1], dp[i-1][j] - prices[i])
                dp[i][j+2] = max(dp[i-1][j+2], dp[i-1][j+1] + prices[i])
        return dp[-1][2*k]
#股票问题永远可以压缩天数维度，但不能压缩交易阶段维度。
#阶段数 = 题目允许的交易次数 × 2。