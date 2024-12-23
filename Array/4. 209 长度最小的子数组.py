#时间复杂度O(n) 空间复杂度O(1)
#滑动窗口法

class Solution:
    def minSubArrayLen(self, s: int, nums: list[int]) -> int:
        l = len(nums)
        left = 0
        right = 0
        min_len = float('inf')
        cur_sum = 0 #当前的累加值

        while right < l:
            cur_sum += nums[right]

            while cur_sum >= s: #当前类价值大于目标值
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1

            right += 1

        return min_len if min_len != float('inf') else 0 #这个写法很好用！