# 单调队列
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])
        
        return ans


#优先级队列
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        max_heap = []
        for i in range(k):
            max_heap.append((-nums[i], i))
        heapq.heapify(max_heap)
        res = [-max_heap[0][0]]

        for i in range(k, len(nums)):
            heappush(max_heap, (-nums[i], i))
            while max_heap[0][1] <= i-k:
                heappop(max_heap)
            res.append(-max_heap[0][0])
        return res