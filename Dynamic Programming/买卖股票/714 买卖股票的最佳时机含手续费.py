#和122买卖股票最佳时机II差不多，只不过这个有手续费
#dp[i][0]持有 dp[i][1]卖出状态

class Solution:
    def maxProfit(self, prices:list[int], fee:int) -> int:
        if len(prices) == 0:
            return 0
        dp = [[0]*2 for _ in range(len(prices))]
        dp[0][0] = -prices[0] #持股票
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][0] + prices[i] - fee, dp[i-1][1])
        return dp[-1][1]
        