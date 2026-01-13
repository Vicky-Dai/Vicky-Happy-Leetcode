class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        un = UnionFind(n)
        for edge in edges:
            s, d = edge
            un.union(s, d)
        return un.get_count()
        
class UnionFind:
    def __init__(self, n):
        self.father = [i for i in range(n)]
        self.rank = [1]*n
        self.count = n

    def find(self, u):
        if self.father[u] != u:
            self.father[u] = self.find(self.father[u])
        return self.father[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return 
        if self.rank[root_u] > self.rank[root_v]:
            self.father[root_v] = root_u
        elif self.rank[root_u] < self.rank[root_v]:
            self.father[root_u] = root_v
        else:
            self.father[root_v] = root_u
            self.rank[root_u] += 1
        self.count -= 1

    def connected(self, u, v):
        return self.father[u] == self.father[v]
    
    def get_count(self):
        return self.count