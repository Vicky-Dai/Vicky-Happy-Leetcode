#dp[i] 以i为结尾的最大连续子数组的和
#递推公式dp[i] = max(dp[i-1]+nums[i], nums[i]) 初始化dp[0] = nums[0] 其他位置同前面的题初始化什么都可以

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        result = dp[0] #最少也有这么个值
        for i in range(len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])  #要么是带上之前的最大值，要么是从我这重新开始
            result = max(result, dp[i])
        return result