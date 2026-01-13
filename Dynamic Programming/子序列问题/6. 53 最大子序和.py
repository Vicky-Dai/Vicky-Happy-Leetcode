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
#你在扫数组，每到一个位置 i：

#看看“把前面的最大和 dp[i-1] 加上我”是不是更好

#如果前面的和已经变成负数，那我直接不要它，从我自己重新开始

#这样 dp[i] 就始终保存“以我作为结尾”的最大和。