# 这道题有多种解法
# dfs
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def dfs(i):
            for j in range(n):
                # 如果 i 和 j 相连 且 j 未访问
                if isConnected[i][j] == 1 and not visited[j]:
                    visited[j] = True
                    dfs(j)

        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1        # 找到一个新的省份
                visited[i] = True
                dfs(i)

        return count
# bfs

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        count = 0
        queue = deque()
        
        for i in range(n):
            if not visited[i]:
                count += 1
                visited[i] = True
                queue.append(i)
                
                while queue:
                    j = queue.popleft()
                    for k in range(n):
                        if isConnected[j][k] == 1 and not visited[k]:
                            visited[k] = True
                            queue.append(k)
        return count

# 并查集

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        rank = [1] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1

        count = n
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    if find(i) != find(j):
                        union(i, j)
                        count -= 1
        return count



