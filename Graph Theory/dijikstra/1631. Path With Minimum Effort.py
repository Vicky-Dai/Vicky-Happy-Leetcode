# Dijikstra 解法
class Solution:
    def minimumEffortPath(self, heights):
        import heapq # 小顶堆优化dijikstra
        # 本题邻接图已经由给出的矩阵提供
        # 每个 (r,c) 是一个点
        # 上下左右是边
        # 边权 = 高度差
        m, n = len(heights), len(heights[0])
        dist = [[float('inf')] * n for _ in range(m)] #minDist数组：minDist数组实际上也是一个placeholder, 用几维数组表示都可以，只要把所有点都表示出来就行
        dist[0][0] = 0
        
        pq = [(0, 0, 0)]  # (effortSoFar, r, c)
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        # 开始dijikstra
        while pq:
            # 选择距离源点最近且未访问过的节点
            effort, r, c = heapq.heappop(pq)
            if r == m-1 and c == n-1:
                return effort  # 提前返回
            
            if effort > dist[r][c]:
                continue
            
            # 更新未访问节点到源点的距离: 
            # 注意这里很有意思，到原点的距离只是一个placeholder，表示从原点到该点的effort，比如本题真正的effort是 高度差，也就是走到目前点的最小
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n:
                    # 当前边权：高度差
                    w = abs(heights[r][c] - heights[nr][nc])
                    # 新 effort = 路径上最大边
                    newEffort = max(effort, w)
                    
                    if newEffort < dist[nr][nc]:
                        dist[nr][nc] = newEffort
                        heapq.heappush(pq, (newEffort, nr, nc))

        return dist[m-1][n-1]


# Union Find 解法
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, size):
                self.parent = [x for x in range(size)]
                self.rank = [0]*(size)

            def find(self, i):
                if self.parent[i] != i:
                    self.parent[i] = self.find(self.parent[i])
                return self.parent[i]

            def union(self, x, y):
                parent_x = self.find(x)
                parent_y = self.find(y)
                if parent_x != parent_y:
                    if self.rank[parent_x] > self.rank[parent_y]:
                        self.parent[parent_y] = parent_x
                    elif self.rank[parent_x] < self.rank[parent_y]:
                        self.parent[parent_x] = parent_y
                    else:
                        self.parent[parent_y] = parent_x
                        self.rank[parent_x] += 1

        row = len(heights)
        col = len(heights[0])
        if row == 1 and col == 1:
            return 0

        edge_list = []
        for current_row in range(row):
            for current_col in range(col):
                if current_row > 0: # 这里是竖着找边，并且0是第一行，所以current_row > 0，如果突然想不明白了可以打印看看
                    difference = abs(
                        heights[current_row][current_col] -
                        heights[current_row - 1][current_col])
                    edge_list.append(
                        (difference, current_row * col + current_col,
                         (current_row - 1) * col + current_col)) # 把二维坐标转换为一维坐标
                if current_col > 0:
                    difference = abs(
                        heights[current_row][current_col] -
                        heights[current_row][current_col - 1])
                    edge_list.append(
                        (difference, current_row * col + current_col, current_row
                         * col + current_col - 1)) 
        edge_list.sort() # 按照边权排序
        union_find = UnionFind(row*col)

        for difference, x, y in edge_list: # 因为从小到大排序，所以第一个连通的边就是最小effort
            union_find.union(x, y)
            if union_find.find(0) == union_find.find(row*col-1):
                return difference
        return -1
