#和300的区别在于，这道题递增必须是连续的
#dp[i]表示以nums[i]结尾的最长连续递增序列的长度，不需要把i之前全都遍历叻
#dp[i] = dp[i-1] + 1 if nums[i] > nums[i-1] else 1

class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        result = 1
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
            result = max(result, dp[i])
        return result