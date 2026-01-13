# dp 定义：dp[j] 表示 和为 j 的组合数
# 可以看作一个完全背包问题，背包容量为 target，物品为 nums，每个物品可以选无限次
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1 # 和为 0 的组合数为 1
        for j in range(1, target+1): # 遍历背包
            for num in nums: # 遍历物品
                if j-num >=0: # 如果背包容量大于等于物品重量
                    dp[j] += dp[j-num] # 状态转移方程
        return dp[-1] # 返回和为 target 的组合数