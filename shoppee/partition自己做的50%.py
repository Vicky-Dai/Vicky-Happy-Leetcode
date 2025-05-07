class Solution:
    def IsPartition(self, nums) :
        # write code here
        nums.sort()
        for point in range(1, len(nums)):
            if sum(nums[:point])==sum(nums[point:len(nums)]):
                return True
        return False