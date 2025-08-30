""" 📌 本质上，这题是一个 多源 BFS（广度优先搜索）问题：
一开始可能有 多个腐烂橘子（多个起点）；

腐烂是按「分钟」传播的，也就是一层一层扩散；

所以我们要的是：从所有起点同时出发，传播最远距离所花的时间（最少轮数）；

这就是经典的 BFS 的最短路径模型，不是 DFS 擅长的场景。 """

""" 🚫 如果你用 DFS，会出什么问题？
1. DFS 是“深度优先”，不能保证最短传播时间
假设你从某个腐烂橘子 (0,0) 开始 DFS，你会一路往下走，可能先腐烂远处的橘子，再回来腐烂近的。

结果是你先污染了远的，再污染近的，近的橘子反而记录了更大的时间 —— 明显不合理！

2. 多个起点同时传播，DFS 处理不了同步性
多个腐烂点同时扩散，在 DFS 中你无法“同时进行多条路径传播”。

DFS 是“先走一条路走到底”，它模拟不出“同一时刻多个腐烂源头扩散”的场景。 """
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        # queue - all starting cells with rotting oranges
        queue = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0)) # ！！注意里面的括号

        def neighbors(r, c) -> (int, int):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc #！！！yield用法 

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d + 1)) # 同一批腐烂的橘子，d的值是相同的

        if any(1 in row for row in grid): # any的用法！！
            return -1
        return d

# yield的作用等于如下代码，生成多个值
def neighbors(r, c):
    res = []
    for nr, nc in ...:
        if ...:
            res.append((nr, nc)) 
    return res




# 我自己写的
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        q =  deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i, j])
        time = self.bfs(grid, q)
        return time if all(cell != 1 for row in grid for cell in row) else -1
    
    def bfs(self, grid, q):
        time = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            time += 1
            for _ in range(len(q)):
                m, n = q.popleft()
                for i, j in directions:
                    x = m + i
                    y = n + j
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                        grid[x][y] = 2
                        q.append([x, y])
        return time-1 if time > 0 else 0
#注意时间，最后一轮没有腐烂的，这时候要减1 