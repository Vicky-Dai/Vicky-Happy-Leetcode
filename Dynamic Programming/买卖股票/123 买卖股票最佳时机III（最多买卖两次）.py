#和之前的区别，就是买卖状态会多一些
#dp[i][0] 不操作 dp[i][1] 第一次持有 dp[i][2]第一次不持有 dp[i][3]第二次持有 dp[i][4] 第二次不持有
#dp[i][1] = max(dp[i-1][1], dp[i-1]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        dp = [[0] * 5 for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        dp[0][3] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][1] = max(dp[i-1][1], - prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
        return dp[-1][4]
    
#这个dp[i][0]完全可以不设置 因为包含了 参考121

#我自己的思考：关于为什么122买卖多次反而也只有两个状态呢？因为在那道题里，只要卖出就会有收益，只要有收益就会卖出，所以只有两个状态，持有和不持有
#而限制次数的，不管是多少次，都得控制数量（在123的表现就是有5个状态，而在188里面的表现就是通过for循环来控制)，并且合理分配达到最大值，所以状态会多一些