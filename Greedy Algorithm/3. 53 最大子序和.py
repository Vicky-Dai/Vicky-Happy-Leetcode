#局部最优：如果连续和为负数，就直接扔掉，因为只会让后面的和变小  ！！！注意！！！这里是连续和，不是遇到负数就扔掉

class Solution:
    def maxSubArray(self, nums):
        result = float('-inf') #初始化结果为负无穷
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > result:
                result = count
            if count <= 0: #连续和对后面的增加没有好处时
                count = 0
            
        return result