#我自己写的：思路和452差不多，但是这里贪心的是，如果遇到重叠得了，把更长的删掉，所以要取min
""" 时间复杂度排序： 先按照 右边界 x[1] 升序排序，时间复杂度是 O(n log n)。
遍历区间： 逐个检查区间是否重叠，并更新非重叠区间的计数。遍历的时间复杂度是 O(n)。
所以总复杂度是nlogn """
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        res = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                res += 1
                intervals[i][1] = min(intervals[i][1], intervals[i-1][1])
        return res