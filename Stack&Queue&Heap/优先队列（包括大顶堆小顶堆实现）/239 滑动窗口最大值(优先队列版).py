class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)] #因为 Python 默认是最小堆，而我们需要 最大堆，所以取负值就能保证堆顶是当前窗口中的最大值。 (-nums[i], i) 是一个元组，所以q变成二维数组
        heapq.heapify(q) #heapq.heapify(q)：将列表 q 转换成一个堆。q 现在是一个最大堆，堆顶元素是窗口中最大的元素（取负值后，最小堆实际上存储的是最大值）。

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        
        return ans
