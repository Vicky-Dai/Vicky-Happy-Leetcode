""" 排序： 先按照 右边界 x[1] 升序排序，时间复杂度是 O(n log n)。
遍历区间： 逐个检查区间是否重叠，并更新箭的数量。遍历的时间复杂度是 O(n)。
所以总复杂度是nlogn """
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if len(points) == 0: return 0
        points.sort(key=lambda x: x[0])
        result = 1 
        for i in range(1, len(points)):
            if points[i][0] > points[i-1][1]:
                result +=1
            else: 
                points[i][1] = min(points[i-1][1], points[i][1])
        return result        

# 排序规则：当起始点相同时，Python的sort()会保持原有相对顺序（稳定排序）
# 但对算法来说，起始点相同时的排列顺序不影响最终结果
# 合并逻辑的数学保证：python复制current_end = min(current_end, end)无论相同起始点的区间如何排列，这个操作都会将合并区间的右边界收缩到当前最小的右端点，相当于自动选择了最"紧凑"的合并方式