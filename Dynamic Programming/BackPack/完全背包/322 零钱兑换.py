#dp[j] 装满容量为j的背包，最少物品为dp[j]
#dp[j] = min(dp[j - coins[i]] + 1, dp[j]); 放不同的物品中取一个最小的
#初始化 dp[0] = 0 根据测试用例 和为0时，凑满的方法一定为0 
#非零下标，考虑，以前求最大值的时候，初始化为0，是为了防止覆盖实际求的过程中产生的最大值
#本道题求最小值，如果还是0的话，每次都会被这个0覆盖，因为0就是最小的，所以要赋值为in最大值
#本道题只是求最小，不要求有没有顺序，所以物品或背包先遍历都可以

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for j in range(coin, amount+1):
                if dp[j - coin] != float('inf'):  # 如果dp[i - coin]不是初始值，则进行状态转移  目的是避免从“无解”状态转移。因为 dp[i - coin] 表示达到 i - coin 所需的最小硬币数量，如果 dp[i - coin] 还是 float('inf')，说明使用当前硬币并不能凑出 i - coin，即还没有办法达到这个状态。
                    dp[j] = min(dp[j], dp[j-coin]+1)
        
# dp[amount] 表示用最少的硬币凑出总金额 amount 的解。如果 dp[amount] 仍然是 float('inf')，就意味着即使遍历了所有硬币也无法凑出 amount，即没有解。这种情况下，返回 -1 表示无解。

        if dp[amount] == float('inf'):  # 如果最终背包容量的最小硬币数量仍为正无穷大，表示无解
            return -1
        return dp[amount]
    
# 第一次遍历到硬币 coin = 1 时：

# for i in range(coin, amount + 1) 会遍历金额 i = 1 到 11。
# 当 i = 1 时，i - coin = 0。由于 dp[0] = 0，即 dp[0] != float('inf')，可以确定 dp[1] = dp[0] + 1 = 1。