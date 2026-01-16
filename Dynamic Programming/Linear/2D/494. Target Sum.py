""" 
DP Bottom UP
dict 稀疏dp
n*m n*m
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)] # dp来记录
        dp[0][0] = 1

        for i in range(n):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count

        return dp[n][target]


""" 
Recursion+ memo(lru cache)
n*m n*m
"""
from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums, target):
        n = len(nums)

        @lru_cache(None)
        def dfs(i, curr):
            if i == n:
                return 1 if curr == target else 0

            return (
                dfs(i + 1, curr + nums[i]) +
                dfs(i + 1, curr - nums[i])
            )

        return dfs(0, 0)


""" 
DP Bottom UP  1 dimensional
dict 稀疏dp
n*m n*m
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total + num] += count
                next_dp[total - num] += count
            dp = next_dp

        return dp[target]