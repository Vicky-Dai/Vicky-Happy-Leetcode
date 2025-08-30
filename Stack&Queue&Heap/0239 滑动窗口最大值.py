from collections import deque

class MyQueue: #单调队列（从大到小
    def __init__(self):
        self.queue = deque()
    
    #每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出。
    #同时pop之前判断队列当前是否为空。
    def pop(self,value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()#list.pop()时间复杂度为O(n),这里需要使用collections.deque()

    def push(self, value):
        while self.queue and value > self.queue[-1]: #例如 当前是[5, 0, 1, 2] 现在还要push一个3进去，那么012全都要弹出 他们三个在队尾也就是入口
            self.queue.pop()
        self.queue.append(value) #如果队尾没有更小的，就放进去

    def front(self): #其实是获取当前窗口最大值，由于在主函数里面前面的方法已经把窗口维护成最大值在最前面 所以取front
        return self.queue[0]    
    
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        que = MyQueue()
        result = []
        #初始化窗口
        for i in range(k): #调用push 将前k的元素放进队列 把小的卷走
            que.push(nums[i])
        result.append(que.front())
        #处理接下来每个窗口
        for i in range(k, len(nums)):
            que.pop(nums[i-k])
            que.push(nums[i]) #顺序很重要 先出再进 否则顺序容易出错
            result.append(que.front())
        return result
    

# 我的写法
# 保存下标而不是值：我们需要知道一个数是否已经滑出窗口。值是无法告诉我们它在哪个位置的，但下标可以轻松判断。
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # 存储的是索引
        res = []
        
        for i in range(len(nums)):
            # 1. 移除窗口外的索引
            if q and q[0] < i - k + 1:
                q.popleft()
            
            # 2. 保持队列单调递减：将比当前值小的都移除
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            
            # 3. 加入当前索引
            q.append(i)
            
            # 4. 记录结果（从第 k-1 项开始）
            if i >= k - 1:
                res.append(nums[q[0]])
        
        return res