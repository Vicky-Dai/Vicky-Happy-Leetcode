class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        if n <= 2:           # 长度小于等于2时直接返回
            return n

        j = 2                # 下一个存放位置，从第三个位置开始
        for i in range(2, n):
            # 只要当前数大于去重后倒数第2个数，就可以保留
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1

        return j
