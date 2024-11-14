#求背包能装的最大重量
#这道题的关键在于想清楚如果能把石头分成重量尽可能相近的两堆，那么它们的差值就是最后石头最小的可能重量
#例如[2, 7, 4, 1, 8, 1] sum = 23 sum/2 = 11  尽可能凑成一个11的背包

class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        _sum = 0
        for stone in stones:
            _sum += stone

        dp = [0] * 15001

        for stone in stones:
            for j in range(_sum//2, stone-1,  -1):
                dp[j] = max(dp[j], dp[j-stone] + stone)
        return _sum - dp[_sum//2] -dp[_sum//2]