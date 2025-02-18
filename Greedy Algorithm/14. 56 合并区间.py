""" 时间复杂度：nlogn """
class Solution:
    def merge(self, intervals):
        result = []
        if len(intervals) == 0:
            return result 
        
        intervals.sort(key = lambda x: x[0])

        result.append(intervals[0]) #直接把第一个区间放进去，因为起码有一个 而且这样下下面方便直接在这个新result上管理

        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(intervals[i][1], result[-1][1])
            else:
                result.append(intervals[i])

        return result
