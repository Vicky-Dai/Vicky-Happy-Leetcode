class UnionFind:
    def __init__(self, n):
        self.n = n
        self.father = list(range(n))  # 初始化每个节点的父节点为自己

    # 查找 u 的根节点，并进行路径压缩
    def find(self, u):
        if self.father[u] != u:
            self.father[u] = self.find(self.father[u])  # 路径压缩
        return self.father[u]

    # 判断 u 和 v 是否在同一个集合
    def is_same(self, u, v):
        return self.find(u) == self.find(v)

    # 合并 u 和 v
    def join(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.father[root_v] = root_u  # 将 root_v 的根节点指向 root_u
