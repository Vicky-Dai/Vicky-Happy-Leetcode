#本题和322零钱兑换是一模一样的
#定义：和为j的完全平方数的最小数量为dp[j]
#递推公式：dp[j] 可以由dp[j - i * i]推出， dp[j - i * i] + 1 便可以凑成dp[j]。
# 此时我们要选择最小的dp[j]，所以递推公式：dp[j] = min(dp[j - i * i] + 1, dp[j]);

#我的写法 j代表背包
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, int(n ** 0.5) + 1):  # 遍历物品
            for j in range(1, n + 1):  # 遍历背包
                if j>=i*i:
                # 更新凑成数字 j 所需的最少完全平方数数量
                    dp[j] = min(dp[j - i * i] + 1, dp[j])

        return dp[n]


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0 #为了递推公式能正常运行

        for i in range(1, n+1): #这个写法也可以，但是可能后面浪费了几轮
            for j in range(i*i, n+1):#当 range(a, b) 中 a > b 时，range 不会生成任何数字，它会返回一个 空的序列。循环也不会执行
                dp[j] = min(dp[j], dp[j - i*i] + 1)  
        return dp[n]