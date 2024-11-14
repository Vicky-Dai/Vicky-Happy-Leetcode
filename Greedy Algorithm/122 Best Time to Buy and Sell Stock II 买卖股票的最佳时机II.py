#局部贪心：单日只要收益为正就买卖

class Solution:
    def buyAndSell(self, nums):
        if len(nums) <= 1:
            return 0
        curP = 0  # 当前一对元素的差值
        preP = nums[0]  # 前一对元素的差值
        result = 0  # 记录峰值的个数，初始为1（默认最右边的元素被视为峰值）
        for i in range(1, len(nums)):
            curP = nums[i]
            diff = curP-preP
            # 如果遇到一个峰值
            if (diff<=0):
                preP = curP
            else:
                result += diff
                preP = curP

        return result
    
#优化
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        result = 0
        for i in range(1, len(prices)):
            result += max(prices[i] - prices[i - 1], 0) #只取正数
        return result