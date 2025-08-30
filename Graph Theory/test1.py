import sys
n, m = map(int, input().split())
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

grid = []
for line in sys.stdin:
    grid.append(list(map(int, line.strip().split())))
visited = [[False]*m for _ in range(n)]
maxA = 0

def dfs(grid, visited, i, j, path):
    if visited[i][j] == False and grid[i][j] == 1:
        path += 1
        visited[i][j] = True
    else: return
    for x, y in direction:
        curX = i + x
        curY = j + y
        if curX < 0 or curX >= n or curY < 0 or curY >= m or grid[i][j] == 0:
            continue
        dfs(grid, visited, curX, curY, path)
    return path

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and visited[i][j] == False:
            cur = dfs(grid, visited, i, j, 0)
            maxA = max(maxA, cur)

print(maxA)