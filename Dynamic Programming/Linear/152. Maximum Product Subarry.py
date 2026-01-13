# 152 compared with 53, the only difference is that we need to consider the negative number
# so we need to maintain two dp arrays, one for the minimum product and one for the maximum product
# the minimum product is used to handle the negative number
# the maximum product is used to handle the positive number
# the state transfer equation is:
# dp1[i] = min(dp1[i-1] * nums[i], dp2[i-1] * nums[i], nums[i])
# dp2[i] = max(dp1[i-1] * nums[i], dp2[i-1] * nums[i], nums[i])
# the base case is:
# dp1[0] = nums[0]
# dp2[0] = nums[0]
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        # 定义：以 nums[i] 结尾的子数组，乘积最小为 dp1[i]
        dp1 = [0] * n

        # 定义：以 nums[i] 结尾的子数组，乘积最大为 dp2[i]
        dp2 = [0] * n

        # base case
        dp1[0] = nums[0]
        dp2[0] = nums[0]

        # 状态转移方程
        for i in range(1, n):
            dp1[i] = self.min(dp1[i - 1] * nums[i], dp2[i - 1] * nums[i], nums[i])
            dp2[i] = self.max(dp1[i - 1] * nums[i], dp2[i - 1] * nums[i], nums[i])

        # 遍历所有子数组的最大乘积，求最大值
        res = float('-inf')
        for i in range(n):
            res = max(res, dp2[i])

        return res

    def min(self, a: int, b: int, c: int) -> int:
        return min(min(a, b), c)

    def max(self, a: int, b: int, c: int) -> int:
        return max(max(a, b), c)