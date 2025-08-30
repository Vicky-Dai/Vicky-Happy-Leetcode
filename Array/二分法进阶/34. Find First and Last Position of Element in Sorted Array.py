class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)
        # 左边界
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else: 
                right = mid
        tl = left
        if tl == len(nums) or nums[tl] != target:
            return [-1, -1]
            
        left, right = 0, len(nums)
        #右边界
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else: 
                left = mid + 1
        tr = left - 1

        return [tl, tr]
