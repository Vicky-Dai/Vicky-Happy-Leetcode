from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        new_arr = [0] * n
        for i in range(n):
            new_arr[(i + k) % n] = nums[i]
        nums[:] = new_arr  # 使用切片赋值以修改原列表
