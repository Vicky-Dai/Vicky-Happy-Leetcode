#把地图中间的1改成0
#本题的标记可以在原来的二维数组上面改，不需要额外的visited数组

def dfs(grid, x, y):
    grid[x][y] = 2
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for dx, dy in directions:
        nextx, nexty = x + dx, y + dy
        #超过边界
        if nextx < 0 or nextx >= len(grid) or nexty < 0 or nexty >= len(grid[0]):
            continue
        if grid[nextx][nexty] == 0 or grid[nextx][nexty] == 2:
            continue
        dfs(grid, nextx, nexty)

def main():
    n, m = map(int, input().split())
    grid = [[int(x) for x in input().split()] for _ in range(n)]

    #步骤一：
    #从左侧边，和右侧边向中间遍历
    for i in range(n):
        if grid[i][0] == 1:
            dfs(grid, i, 0)
        if grid[i][m-1] == 1:
            dfs(grid, i, m-1)
    #从上边和下边 向中间遍历
    for i in range(m):
        if grid[0][j] == 1:
            dfs(grid, 0, j)
        if grid[n-1][j] == 1:
            dfs(grid, n - 1, j)
    #步骤二、三
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                grid[i][j] = 0  #把不连接外围的岛屿都沉没
            if grid[i][j] == 2:
                grid[i][j] = 1

    #打印结果
    for row in grid:
        print(''.join(map(str, row)))

if __name__ == "__main__":
    main()