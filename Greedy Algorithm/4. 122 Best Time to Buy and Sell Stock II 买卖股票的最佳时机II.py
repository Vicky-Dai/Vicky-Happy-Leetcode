#局部贪心：单日只要收益为正就买卖
""" 时间复杂度 O(n) """

#DK版
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                res += prices[i] - prices[i-1]
        return res
        
    
#优化
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        result = 0
        for i in range(1, len(prices)):
            result += max(prices[i] - prices[i - 1], 0) #只取正数
        return result