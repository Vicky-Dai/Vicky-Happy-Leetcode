# 二分法的精髓就在于，每次能去掉一半，至于去的条件要具体问题具体分析
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]: # 看看是在左半边还是右半边
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
        return res