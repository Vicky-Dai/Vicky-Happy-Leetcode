from collections import deque

#处理输入
n, m = list(map(int, input().split()))
g = []
for _ in range(n):
    row = list(map(int, input().split))
    g.append(row)

#定义四个方向、孤岛的面积（遍历完边缘后会被重置
directions = [[0,1], [1,0], [-1,0], [0,-1]]
count = 0

#广搜
def bfs(r, c):
    global count 
    q = deque()
    q.append((r, c))
    g[r][c] = 0
    count += 1

    while q:
        r, c = q.popleft() #每一层都按顺序，从左边取值，看这个值的周围有没有没访问的
        for di in directions:
            next_r = r + di[0]
            next_c = c + di[1]
            if next_c < 0 or next_c >= m or next_r < 0 or next_r >= n:
                continue 
            if g[next_r][next_c] == 1:
                q.append((next_r, next_c))
                g[next_r][next_c] = 0
                count += 1

for i in range(n):
    if g[i][0] == 1: bfs(i, 0)
    if g[i][m - 1] == 1: bfs(i, m-1)

for i in range(m):
    if g[0][i] == 1: bfs(n-1, i)
    if g[n-1][i] == 1: bfs(n-1, i)

count = 0 #初始化结果，第二次遍历
for i in range(n):
    for j in range(m):
        if g[i][j] == 1: bfs(i, j)

print(count)