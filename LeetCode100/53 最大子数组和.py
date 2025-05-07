# 贪心算法 count: 记录当前遍历过程中的子数组和。如果 count 超过了 result，就更新 result。
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > result:
                result = count
            if count <= 0:
                count = 0
        return result
    
#动态规划 Kadane’s Algorithm
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0  # 记录以当前元素结尾的最大子数组和
        max_ans = nums[0]  # 记录目前找到的最大子数组和
        for x in nums:  # 遍历数组
            pre = max(pre + x, x)  # 选择是累加前面的结果还是重新开始
            max_ans = max(max_ans, pre)  # 更新全局最大子数组和
        return max_ans  # 返回最终的最大和

#如果按照传统 DP 的思路，我们可以定义：
#dp[i] 表示以 nums[i] 结尾的最大子数组和。
#Kadane’s Algorithm 就是对 DP 进行了优化，不使用额外的数组存储 dp[i]，而是直接用变量 pre 代替！