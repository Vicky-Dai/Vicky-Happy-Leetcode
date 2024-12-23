from typing import List
from collections import defaultdict

class Solution:
    def __init__(self):
        self.direction = [(1,0), (-1,0), (0, 1), (0, -1)]
        self.res = 0
        self.count = 0
        self.idx = 1
        self.count_area = defaultdict(int)

    def max_area_island(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.count = 0  #????
                    self.idx += 1
                    self.dfs(grid, i, j)
        #print(grid) ????????
        self.check_area(grid) # ????
        # print(self.count_area) ????
        if self.check_largest_connect_island(grid = grid):
            return self.res + 1

    def dfs(self, grid, row, col):
        grid[row][col] = self.idx
        self.count += 1
        for dr, dc in self.direction:
            _row = dr + row
            _col = dc + col
            if 0<=_row<len(grid) and 0<=_col<len(grid[0]) and grid[_row][_col] == 1:
                self.dfs(grid, _row, _col)
        return
    
    def check_area(self, grid):
        m, n = len(grid), len(grid[0])
        for row in range(m):
            for col in range(n):
                self.count_area[grid[row][col]] = self.count_area.get(grid[row][col], 0) + 1
        return
    
    def check_largest_connect_island(self, grid):
        m, n = len(grid), len(grid[0])
        has_connect = False
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    has_connect = True
                    area = 0
                    visited = set()
                    for dr, dc in self.direction:
                        _row = row + dr 
                        _col = col + dc
                        if 0<=_row<len(grid) and 0<=_col<len(grid[0]) and grid[_row][_col] != 0 and grid[_row][_col] not in visited:
                            visited.add(grid[_row][_col])
                            area += self.count_area[grid[_row][_col]]
                            self.res = max(self.res, area)
                            
        return has_connect




def main():
    m, n = map(int, input().split())
    grid = []

    for i in range(m):
        grid.append(list(map(int,input().split())))

    
    sol = Solution()
    print(sol.max_area_island(grid))

if __name__ == '__main__':
    main()



#List和list的区别就是List支持定义的时候显示声明嵌套类型定义比如List[int], 而后者是内置数据结构list = [] 直接创建

#简化版本
from typing import List
from collections import deque, defaultdict

class Solution:
    def max_area_island(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # 用于记录每个岛屿的编号以及其面积
        island_id = [[-1] * cols for _ in range(rows)] #创建一个与 grid 大小相同的二维数组 island_id，用于标记每个格子所属于的岛屿的编号。每个元素的初始值设置为 -1，表示还没有给该格子分配岛屿编号。
        island_area = defaultdict(int) #创建一个 defaultdict，用来记录每个岛屿编号对应的岛屿面积。
        island_counter = 0 #初始化一个计数器 island_counter，用于为每个新岛屿分配一个唯一的编号。
        
        # 广度优先搜索，用来计算岛屿的面积
        def bfs(row: int, col: int, id: int) -> int:
            queue = deque([(row, col)]) # 它可以接受一个可迭代对象（如列表、元组等）作为初始化数据。[(row, col)]：这是一个包含单一元组 (row, col) 的列表。元组 (row, col) 通常表示某个网格的坐标。例如，(row, col) 可以表示二维网格中的一个位置。
            island_id[row][col] = id #给当前遍历的岛屿编号
            area = 1 #在开始遍历某个岛屿时，我们先将当前格子 (row, col) 作为岛屿的第一个格子，所以面积初始化为 1。
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and island_id[nr][nc] == -1: #没超出范围 陆地 且没有标号
                        island_id[nr][nc] = id
                        area += 1
                        queue.append((nr, nc))
            return area
        
        # 第一步：遍历网格，将每个岛屿标号并计算其面积
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and island_id[r][c] == -1:
                    # 新岛屿发现，给它一个编号
                    area = bfs(r, c, island_counter)
                    island_area[island_counter] = area
                    island_counter += 1
        
        max_area = 0
        
        # 第二步：遍历每个水域格子（0），尝试将其改为陆地
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    # 记录相邻的岛屿编号
                    adjacent_islands = set()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            adjacent_islands.add(island_id[nr][nc])
                    
                    # 如果水域可以连接多个岛屿，计算它们合并后的面积
                    area = 1  # 变成陆地的面积为1
                    for island in adjacent_islands:
                        area += island_area[island]
                    
                    max_area = max(max_area, area)
        
        # 如果没有水域可以改变，则返回最大岛屿面积
        return max(max_area, max(island_area.values(), default=0)) #max(island_area.values()) 会返回 island_area 中所有岛屿面积的最大值。如果字典为空，max() 函数会引发 ValueError 错误。为了解决这个问题，我们使用了 default=0 参数，它指定当 island_area 为空时，max() 函数返回 0 而不是抛出错误。

def main():
    m, n = map(int, input().split())
    grid = []
    for _ in range(m):
        grid.append(list(map(int, input().split())))
    
    sol = Solution()
    print(sol.max_area_island(grid))

if __name__ == '__main__':
    main()
