#dp[i][0] = 在第 i 天结束时，处于「不持有股票」状态下的最大利润
#dp[i][0] 持有股票的最大收益 dp[i][1] 不持有股票的最大收益 持有不持有不是当天瞬时状态，而是截止到当天的状态
#dp[i][0] = max(dp[i-1][0], -prices[i]) 可以理解为在过去寻找最低的买入价格 dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i]) 理解为找到最合适的卖出价格
#初始化 dp[0][0] = -prices[0]第零天持有就是必须买入，手里的钱变成负数 dp[0][1] = 0 什么都不做就是0

class Soltion:
    def maxProfit(self, prices: list[int]) -> int:
        length = len(prices)
        if length == 0:
            return 0
        dp = [[0]*2 for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], -prices[i]) # 
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        return dp[-1][1] #肯定是走到最后一天，以及最后一天如果还是持有，因为本道题只能买卖一次，一直没卖说明不可能比卖掉收益更大
    

#brute force
#两层for

#贪心算法：贪心算法可以解决个别股票问题
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low = float("inf")
        result = 0
        for i in range(len(prices)):
            low = min(low, prices[i])#取最左最小价格
            result = max(result, prices[i]-low) #最大区间利润
        return result