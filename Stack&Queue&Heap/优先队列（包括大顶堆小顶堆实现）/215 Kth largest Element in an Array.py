import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 使用最小堆来保存前 k 个最大元素
        min_heap = []

        for num in nums:
            # 将当前元素推入堆
            heapq.heappush(min_heap, num)
            
            # ！！！！顺序 先push再pop 如果堆的大小超过 k，移除堆顶元素
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # 堆顶元素即为第 k 大的元素
        return min_heap[0]




