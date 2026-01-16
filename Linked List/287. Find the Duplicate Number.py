#👉 把数组本身当成“访问标记表”

#每个数字 x 对应数组下标 x-1
#第一次看到 x：把 nums[x-1] 变成负数（做标记）
#第二次看到 x：发现 nums[x-1] 已经是负数 → x 就是重复数
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums :
            idx = abs(num) - 1
            if nums[idx] < 0 :
                return abs(num)
            nums[idx] *= -1
        return -1
