from collections import deque

n, m = list(map(int, input().split()))
g = []
for _ in range(n):
    row = list(map(int, input().split()))
    g.append(row)

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
count = 0

def bfs(r,c,mode):
    global count 
    q = deque()
    q.append((r,c))
    count += 1
    
    while q:
        r, c = q.popleft()
        if mode:
            g[r][c] = 2
            
        for di in directions:
            next_r = r + di[0]
            next_c = c + di[1]
            if next_c < 0 or next_c >= m or next_r < 0 or next_r >= n:
                continue
            if g[next_r][next_c] == 1:
                q.append((next_r,next_c))
                if mode:
                    g[r][c] = 2
                    
                count += 1
    

for i in range(n):
    if g[i][0] == 1: bfs(i,0,True)
    if g[i][m-1] == 1: bfs(i, m-1,True)
    
for j in range(m):
    if g[0][j] == 1: bfs(0,j,1)
    if g[n-1][j] == 1: bfs(n-1,j,1)

for i in range(n):
    for j in range(m):
        if g[i][j] == 2:
            g[i][j] = 1 #把2改成1
        else:
            g[i][j] = 0 #剩下的保持0
            
for row in g:
    print(" ".join(map(str, row)))