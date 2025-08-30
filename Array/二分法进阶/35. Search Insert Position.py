class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) # 最后一个位置也可以插入
        while left < right: # 找的是大于等于不是固定某个值，所以用左闭右开比较好
            mid = (left + right) // 2
            if nums[mid] < target: # 而题目是找 第一个大于等于 target 的位置，所以条件应该是 if nums[mid] < target，然后移动 left，否则移动 right
                left = mid+1 # 注意left = mid容易死循环
            else:
                right = mid
        return left
            