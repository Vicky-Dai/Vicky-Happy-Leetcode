""" MinHeap
nlogn + mlogm
n+m """
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # queries.sort()
        intervals.sort()
        res = {}
        i = 0
        hq = []
        for q in sorted(queries):
            # 先把一个q对应的可能的区间都放进去
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(hq, ((intervals[i][1] - intervals[i][0] + 1), intervals[i][1]))
                i += 1

            #先筛掉end不在范围的 然后heapq顶端就是最短的
            while hq and hq[0][1] < q:
                heapq.heappop(hq)
            res[q] = hq[0][0] if hq else -1
        return [res[q] for q in queries]
