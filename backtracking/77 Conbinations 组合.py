class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result  = [] #存放结果集合 局部变量
        self.backtracking(n, k, 1, [], result)
        return result
        
    def backtracking(self, n, k, startIndex, path, result): #backtracking 函数接收到的 result 其实是 combine 函数中定义的 result 的引用。因此，无论在 combine 还是 backtracking 中对 result 进行修改，修改的都是同一个列表对象。
#在这两个函数中，虽然 result 在名称上是相同的，但它们本质上是局部变量。每个函数中的 result 都是其各自的局部变量。局部变量的名称可以不同，但只要你传递的是同一个对象，它们实际上指向的就是同一个对象。
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(startIndex, n + 1):  # 需要优化的地方
            path.append(i) #处理节点
            self.backtracking(n, k, i+1, path, result)
            path.pop() #回溯，撤销处理的节点


#优化版本
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []  # 存放结果集
        self.backtracking(n, k, 1, [], result)
        return result
    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(startIndex, n - (k - len(path)) + 1):  # 优化的地方 开始选点的地方，最多不能超过n-(k-len(path) +1)
            #n是数组长度，k是我需要选取的个数，len（path）是选了的，那么k-len(path)就是我还得拿几个数，那么我得保证n的后侧还至少省那么多数，反过来就是前面最多能从哪取，+1是为了保证最后一个需要的点能取到（因为左闭右开）
            path.append(i)  # 处理节点
            self.backtracking(n, k, i + 1, path, result)
            path.pop()  # 回溯，撤销处理的节点