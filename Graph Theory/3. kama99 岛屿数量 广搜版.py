#这里有一个广搜中很重要的细节：

#根本原因是只要 加入队列就代表 走过，就需要标记，而不是从队列拿出来的时候再去标记走过。

from collections import deque
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(grid, visited, x, y):
    que = deque([])
    que.append
    visited[x][y] = True
    while que:
        cur_x, cur_y = que.popleft()
        for i, j in directions:
            next_x = cur_x + i
            next_y = cur_y + j
            if next_y < 0 or next_x < 0 or next_x >= len(grid) or next_y >= len(grid[0]):
                continue #越界跳过
            if not visited[next_x][next_y] and grid[next_x][next_y] == 1: #没有visit过并且是陆地
                visited[next_x][next_y] = True
                que.append((next_x, next_y))

def main():
    n, m = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split()))) #邻接表二维数组
    visited = [[False] * m for _ in range(n)] #访问表，用于标记是否访问过
    res = 0 #岛屿数量

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]: #找到陆地并且没有访问过
                res += 1
                bfs(grid, visited, i, j)
    print(res)

if __name__ == "__main__":
    main