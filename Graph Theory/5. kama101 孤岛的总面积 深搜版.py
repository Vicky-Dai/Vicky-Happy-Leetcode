#本题要求找到不靠边的陆地面积!!理解这个很重要，那么我们只要从周边找到陆地然后 通过 dfs或者bfs 将周边靠陆地且相邻的陆地都变成海洋，然后再去重新遍历地图 统计此时还剩下的陆地就可以了。
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
result = 0

#深度搜索
def dfs(grid, x, y):
    grid[x][y] = 0
    global result
    result += 1 #下面每次调用dfs的时候都是因为找到一个陆地（格子是1）

    for i, j in direction:
        next_x = x + i
        next_y = y + j
        if (next_x < 0 or next_y <0 or next_y >= len(grid[0]) or next_y >= len(grid)):
            continue
        if  grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
            visited[next_x][next_y] = True
            dfs(grid, next_x, next_y)

#读取
n, m = map(int, input())
grid = []
visited = [[False] for _ in range(n)]

for i in range(n):
    grid.append(list(map(int, input().split())))

#！！！！！！！！ 单独处理 处理边界  把边界上的陆地都改成海洋
for j in range(m):
    #上边界
    if grid[0][j] == 1 and not visited[0][j]:
        visited[0][j] = True
        dfs(grid, 0, j)

    #下边界
    if grid[n - 1][j] == 1 and not visited[n - 1][j]:
        visited[n - 1][j] = True
        dfs(grid, n-1, j)

for i in range(n):
    #左边界
    if grid[i][0] == 1 and not visited[i][0]:
        visited[i][0] = True
        dfs(grid, i, 0)
    
    #右边界
    if grid[i][m - 1] == 1 and not visited[i][m-1]:
        visited[i][m-1] = True
        dfs(grid, i, m-1)

#计算孤岛面积：边界上的陆地都改成海洋了之后，还剩下的中间没访问过的陆地就是孤岛
result = 0 # ！！！！！！！！！初始化，避免使用到处理边界时产生的累加值

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            dfs(grid, i, j)

#输出孤岛的总面积
print(result)
