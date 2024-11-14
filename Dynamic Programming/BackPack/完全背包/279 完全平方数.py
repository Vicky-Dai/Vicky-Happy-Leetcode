#本题和322零钱兑换是一模一样的
#定义：和为j的完全平方数的最小数量为dp[j]
#递推公式：dp[j] 可以由dp[j - i * i]推出， dp[j - i * i] + 1 便可以凑成dp[j]。
# 此时我们要选择最小的dp[j]，所以递推公式：dp[j] = min(dp[j - i * i] + 1, dp[j]);

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0 #为了递推公式能正常运行

        for i in range(1, n+1):
            for j in range(i*i, n+1):
                dp[j] = min(dp[j], dp[j - i*i] + 1)
        return dp[n]