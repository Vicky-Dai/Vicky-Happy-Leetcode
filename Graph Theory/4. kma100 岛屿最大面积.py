#四个方向
position = [[0,1], [1, 0], [0, -1], [-1, 0]]
count = 0

def dfs(grid, visited, x, y):
    """ 深度优先搜索，对一整块陆地进行标记 """
    global count # 全局变量，便于传递count值
    for i, j in position:
        cur_x = x + i
        cur_y = y + j
        #终止条件 下标越界，跳过
        if cur_x < 0 or cur_x >= len(grid) or cur_y < 0 or cur_y >= len(grid[0]):
            continue
        if not visited[cur_x][cur_y] and grid[cur_x][cur_y] == 1:
            visited[cur_x][cur_y] = True
            count += 1
            dfs(grid, visited, cur_x, cur_y)  #走完到下一个for就是回溯

n, m = map(int, input().split()) #获取输入
#邻接矩阵
grid = []
for i in range(n):
    grid.append(list(map(int, input().split()))) # 用户的任何输入都是String类型，所以需要map遍历转换成int类型
#访问表
visited = [[False]*m for _ in range(n)]

result = 0 # 记录最终结果
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and not visited [i][j]:
            count = 1
            visited[i][j] = True
            dfs(grid, visited, i, j)
            result = max(count, result)

print(result)

#这种回溯和全排列找路径46的回溯有什么区别？ 这种不用记录路径，走完当前的路径forloop到下一个路径本身就是回溯，但是46那种要自己记录路径的，也要自己把路径回溯
