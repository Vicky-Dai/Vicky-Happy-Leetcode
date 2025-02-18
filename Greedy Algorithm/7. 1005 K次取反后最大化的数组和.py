""" * """ #递减排序
    
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key = lambda x:abs(x), reverse = True )#!!!!按照绝对值从大到小排序，这样负数最大的就可以先取反
        
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
        if k%2 == 1:
            nums[-1] = -nums[-1] #最后一个数取反 (因为是排序过的，所以最后一个数一定是最小的) 0的情况直接在这里处理了
        return sum(nums)