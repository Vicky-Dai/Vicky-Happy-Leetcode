""" 对于每个位置 i：
    找出所有 j<i 且 nums[j]<nums[i] 中 dp[j] 最大的
    dp[i] = dp[j] + 1 """
# Time O(n2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        dp = [1] * len(nums)
        result = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1) #注意这里是dp[j] + 1 所以可以正常运行 ！！再看看
            result = max(result, dp[i]) #取长的子序列
        return result
    


#     让我们通过详细的步骤来分析序列 [2, 1, 3, 4, 5]，并解释为什么不会出问题。

# 初始化
# 首先，初始化 dp 数组和 result 变量：

# 迭代过程
# 我们通过嵌套的 for 循环来更新 dp 数组和 result 变量。

# 第 1 天
# i = 1:

# j = 0: nums[1] = 1 不大于 nums[0] = 2，所以 dp[1] 不变。
# dp = [1, 1, 1, 1, 1] result = 1

# 第 2 天
# i = 2:

# j = 0: nums[2] = 3 大于 nums[0] = 2，所以 dp[2] = max(dp[2], dp[0] + 1) = 2
# j = 1: nums[2] = 3 大于 nums[1] = 1，所以 dp[2] = max(dp[2], dp[1] + 1) = 2
# dp = [1, 1, 2, 1, 1] result = 2

# 第 3 天
# i = 3:

# j = 0: nums[3] = 4 大于 nums[0] = 2，所以 dp[3] = max(dp[3], dp[0] + 1) = 2
# j = 1: nums[3] = 4 大于 nums[1] = 1，所以 dp[3] = max(dp[3], dp[1] + 1) = 2
# j = 2: nums[3] = 4 大于 nums[2] = 3，所以 dp[3] = max(dp[3], dp[2] + 1) = 3
# dp = [1, 1, 2, 3, 1] result = 3

# 第 4 天
# i = 4:

# j = 0: nums[4] = 5 大于 nums[0] = 2，所以 dp[4] = max(dp[4], dp[0] + 1) = 2
# j = 1: nums[4] = 5 大于 nums[1] = 1，所以 dp[4] = max(dp[4], dp[1] + 1) = 2
# j = 2: nums[4] = 5 大于 nums[2] = 3，所以 dp[4] = max(dp[4], dp[2] + 1) = 3
# j = 3: nums[4] = 5 大于 nums[3] = 4，所以 dp[4] = max(dp[4], dp[3] + 1) = 4
# dp = [1, 1, 2, 3, 4] result = 4