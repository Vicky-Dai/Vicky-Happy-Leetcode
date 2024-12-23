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