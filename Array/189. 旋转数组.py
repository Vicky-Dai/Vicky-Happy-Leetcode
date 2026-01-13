#方法一：局部翻转 + 整体翻转
class Solution:
    def rotate(self, A: List[int], k: int) -> None:
        def reverse(i, j):
            while i < j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
        n = len(A)
        k %= n
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

# 我写的  但是空间复杂度是0
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k%len(nums)
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        copy = nums[:]

        for i in range(len(nums)):
            nums[(i + k) % len(nums)] = copy[i]
        
        return nums

        # 备注：这个方法会导致空间复杂度变成 O(n) 因为我们要创建一个 copy 数组。但是不失为一种思路。