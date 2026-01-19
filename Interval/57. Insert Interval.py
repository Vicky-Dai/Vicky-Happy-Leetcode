# binary search
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:      
        # Find the first index i such that intervals[i][0] >= newInterval[0].
        target = newInterval[0]
        left, right = 0, len(intervals)
        while left < right:
            mid = (left + right)//2
            if intervals[mid][0] >= target:
                right = mid
            else:
                left = mid + 1
        
        res = []
        intervals.insert(left, newInterval)
        # sweep line merging
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

# Linear Search
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """ 
        Solve probelem in linear way 
        1. while loop to add the intervals before newInterval
        2. while loop to see when we insert newInterval, we need
        to combine all the intervals we need
        3. while loop to intervals end the rest of intervals
        """
        i = 0
        res = []
        n = len(intervals)
        # 1   remember i<n!!!
        while i< n and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1
        
        # 2
        while i<n and newInterval[1] >= intervals[i][0]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        res.append(newInterval)

        # 3 
        while i < n:
            res.append(intervals[i])
            i += 1
        return res


# Greedy Solution
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        res.append(newInterval)
        return res
