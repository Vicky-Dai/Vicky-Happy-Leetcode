#时间复杂度 O(n^2)

import collections
directions = [[-1,0], [0,1], [0,-1], [1,0]]
area = 0

def dfs(i, j, grid, visited, num):
    global area

    if visited[i][j]:
        return 
    
    visited[i][j] = True
    grid[i][j] = num
    area += 1

    for x, y in directions:
        new_x = i + x
        new_y = j + y
        if (
            0 <= new_x <len(grid)
            and 0 <= new_y < len(grid[0])
            and grid[new_x][new_y] == "1"
        ):
             dfs(new_x, new_y, grid, visited, num)

def main():
    global area

    N, M = map(int, input().strip().split())
    grid = []
    for i in range(N):
        grid.append(input().strip().split())
    visited = [[False]*M for _ in range(N)]
    rec = collections.defaultdict(int)

    cnt = 2
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "0": #遍历所有海洋
                max_island = 1 #水变成陆地，从1开始计数
                v = set() #用于保存岛屿编号，有效避免重复，并且每个水变陆地的时候，把这个避免重复的v清空
                for x, y in directions: #检查邻居岛屿并累加面积
                    new_x = i + x
                    new_y = j + y
                    if (
                        0 <= new_x < len(grid)
                        and 0 <= new_y < len(grid[0])
                        and grid[new_x][new_y] != "0"
                        and grid[new_x][new_y] not in v
                    ):
                        max_island += rec[grid[new_x][new_y]]
                        v.add(grid[new_x][new_y])
                res = max(res, max_island)

    if res == 0:
        return max(rec.values())
    return res

if __name__ == "__main__":
    print(main())


""" rec = collections.defaultdict(int) 是用 Python 的 collections 模块创建一个默认字典 (defaultdict)。它的行为和普通字典类似，但具有一个关键区别：当访问一个不存在的键时，defaultdict 会自动为这个键创建一个默认值，而不会抛出 KeyError。 """

# 我自己写的
def dfs(grid, i, j, count, a):
    directions = [(-1,0), (1,0), (0,1), (0,-1)]
    grid[i][j] = count
    a += 1
    for d in directions:
        ni = i+d[0]
        nj = i+d[1]
        if 0<=ni<len(grid) and 0<=nj<len(grid[0]) and grid[ni][nj] == 1:
            dfs(grid, ni, nj, count, a)

n, m = map(int, input().split())
grid = []
count = 1
for i in range(n):
    grid.append(list(map(int, input().split())))
area = {}
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            a = 0
            count += 1
            dfs(grid, i, j, count, a)
            area[count] = a

maxIsland = 0
for i in range(n):
    for j in range(m):
        island = 1
        if grid[i][j] == 0:
            record = set()
            directions = [(-1,0), (1,0), (0,1), (0,-1)]
            for d in directions:
                ni = i+d[0]
                nj = i+d[1]
                if 0<=ni<len(grid) and 0<=nj<len(grid[0]) and grid[ni][nj]!= 0 and grid[ni][nj] not in record:
                    island += area[grid[ni][nj]]
                    record.add(grid[ni][nj])
        maxIsland = max(maxIsland, island)
print(maxIsland)


class Solution:
    def largestIsland(self, grid):
        n, m = len(grid), len(grid[0])
        area = {}
        count = 2  # 从2开始标记岛屿
        directions = [(-1,0), (1,0), (0,1), (0,-1)]

        def dfs(i, j, idx):
            grid[i][j] = idx
            a = 1
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                    a += dfs(ni, nj, idx)
            return a

        # 标记每个岛屿并统计面积
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area[count] = dfs(i, j, count)
                    count += 1

        res = max(area.values(), default=0)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    seen = set()
                    total = 1
                    for d in directions:
                        ni, nj = i + d[0], j + d[1]
                        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] > 1 and grid[ni][nj] not in seen:
                            total += area[grid[ni][nj]]
                            seen.add(grid[ni][nj])
                    res = max(res, total)
        return res

if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    sol = Solution()
    print(sol.largestIsland(grid))

# 改进封装的版本