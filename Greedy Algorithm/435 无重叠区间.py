class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if len(intervals) == 0: return 0
        intervals.sort(key = lambda x: x[0])
        result = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[i-1][1]:
                continue
            else: 
                result += 1
                intervals[i][1] = min(intervals[i][1], intervals[i-1][1]) #注意这里是min！！ 否则会重复算一次

        return result
