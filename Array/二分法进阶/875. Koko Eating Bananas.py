""" 💡 观察与思路：
速度越大，吃得越快，用的时间越少 ⇒ 满足单调性

目标：找出最小的 k，满足“能在 h 小时内吃完”

这就转化成了一个最小满足条件的值的二分搜索问题！ """

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right)//2
            if self.canFinish(piles, h, mid):
                right = mid
            else: 
                left = mid+1
        return left

    def canFinish(self, piles, h, k):
        time = 0
        for pile in piles:
            t = (pile + k - 1) // k
            time += t
        return time <= h

    
# 借鉴AI
import math

def minEatingSpeed(piles, h):
    left, right = 1, max(piles)

    def can_finish(k):
        return sum(math.ceil(p / k) for p in piles) <= h

    while left < right:
        mid = (left + right) // 2
        if can_finish(mid):
            right = mid
        else:
            left = mid + 1

    return left
