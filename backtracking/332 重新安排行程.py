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