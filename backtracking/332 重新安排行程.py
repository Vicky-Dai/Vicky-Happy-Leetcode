""" * """
""" 整体时间复杂度由两个主要部分组成：
Python 使用的排序算法是 Timsort（基于 归并排序 和 插入排序 的混合算法）。Timsort 是一种稳定的排序算法，在最坏情况下的时间复杂度为 O(n log n)。
排序部分：O(n log n)。
DFS 遍历部分：O(n)。
因此，整体的时间复杂度是 O(n log n)，其中 n 是机票的数量。 """
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        self.adj = {}

        # sort by the destination alphabetically
        # 根据航班每一站的重点字母顺序排序
        tickets.sort(key=lambda x:x[1]) #这是一个匿名函数（lambda 表达式）。在这里，它接收一个参数 x（代表 tickets 列表中的每个元素），并返回该元素的第二个值（即 x[1]）。因此，列表将根据每个元素的第二个值进行排序。
#key: 这是 sort() 方法的一个参数。它允许我们指定一个函数，该函数在排序时将被调用来提取每个元素的排序键。换句话说，key 参数指定了用于比较的值。
#sort方法对于数字字母都能排序，因为背后都是ASCII码或unicode

        # get all possible connection for each destination
        # 罗列每一站的下一个可选项
        for u,v in tickets:
            if u in self.adj: self.adj[u].append(v)
            else: self.adj[u] = [v]
# self.adj = {
#     'A': ['B', 'C'],  # 从 A 出发到 B 和 C
#     'B': ['D'],       # 从 B 出发到 D
# }
        # 从JFK出发
        self.result = []
        self.dfs("JFK")  # start with JFK

        return self.result[::-1]  # reverse to get the result 因为在 DFS 的过程中，结果是反向的，所以需要反转一下。

    def dfs(self, s):
        # if depart city has flight and the flight can go to another city
        while s in self.adj and len(self.adj[s]) > 0:
            # 找到s能到哪里，选能到的第一个机场
            v = self.adj[s][0]  # we go to the 1 choice of the city
            # 在之后的可选项机场中去掉这个机场
            self.adj[s].pop(0)  # get rid of this choice since we used it
            # 从当前的新出发点开始
            self.dfs(v)  # we start from the new airport

        self.result.append(s)  # after append, it will back track to last node, thus the result list is in reversed order
#因为每个航班 都只访问一次，所以不会出现无限循环。

#纯代码版
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.adj = {}
        tickets.sort(key=lambda x:x[1]) 
        s = "JFK"
        for u, v in tickets: # 似乎必须要用这个字典，因为要保证所有的机票都用完，至于怎么放，交给回溯
            if u in self.adj:
                self.adj[u].append(v)
            else:
                self.adj[u] = [v]
        res = []
        self.backtracking(res, s)
        return res[::-1]
    
    def backtracking(self, res, s):
        while s in self.adj and len(self.adj[s])>0:
            v = self.adj[s][0]
            self.adj[s].pop(0)
            self.backtracking(res, v)
        res.append(s)