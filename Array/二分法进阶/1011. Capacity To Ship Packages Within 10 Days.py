#我自己写的
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # descending   left edge
        left, right = 0, 0
        for w in weights:
            left = max(left, w)
            right += w
        while left < right:
            mid = (left+right) // 2
            if self.f(mid, weights) > days:
                left = mid+1
            else:
                right = mid  # when we want to find left edge, we need to leave the = in the right condition, since we want the right index shrink
        return left 

    def f(self, x, weights):
        i = 0
        d = 0
        while i < len(weights):
            d += 1
            ship = x
            while i < len(weights) and weights[i] <= ship: # ！！！！first make sure not out of range
                ship -= weights[i]
                i += 1
        return d


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 0
        right = 0
        for w in weights:
            left = max(left, w)
            right += w

        while left < right:
            mid = left + (right - left) // 2
            if self.f(weights, mid) <= days:
                right = mid
            else:
                left = mid + 1
        return left
    
    def f(self, weights: List[int], x: int) -> int:
        days = 0
        i = 0
        while i < len(weights):
            cap = x # when overloaded, it is reset
            while i < len(weights):
                if cap < weights[i]:
                    break
                cap -= weights[i]
                i += 1
            days += 1
        return days
    
"""
感觉while函数难写？
1. 先用自然语言写出流程
不要一上来就写代码，先把操作流程像写菜谱一样写下来，比如你的问题可以这样描述：

从第一个货物开始，今天有 cap = x 的空间：

如果当前货物能放得下，就放上去，减少剩余空间 cap，然后看下一个货物。

如果放不下，今天结束（船出发），进入下一天。

重复这个过程，直到所有货物装完。

当你能用这种“生活化的步骤”写出来时，代码几乎是直接翻译。 """