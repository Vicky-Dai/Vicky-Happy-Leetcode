# grid[i][j] = Sij
import sys
sys.setrecursionlimit(1000000) # 把 Python 最大递归深度调高。
def main():
    # 优化输入
    data = sys.stdin.read().split()
    it = iter(data) # 把 list 变成迭代器，可以理解成data = ["3","3","baa"...]，但是it是一个指针
    n = int(next(it)) #从迭代器取下一个元素。
    m = int(next(it))
    
    grids = [next(it) for _ in range(n)] # 等价于grids = []
# for _ in range(n):
#     grids.append(next(it))
    
    # 方向数组：右、下、左、上
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # connect数组记录每个点所属的连通块编号
    connect = [[0] * m for _ in range(n)]
    vis = [[False] * m for _ in range(n)]
    idx = 1  # 连通块编号从1开始
    
    def dfs(x, y, current_idx):
        """深度优先搜索标记连通块"""
        connect[x][y] = current_idx
        vis[x][y] = True
        tribe = grids[x][y]  # 当前部族字符
        
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            # 检查边界、是否访问过、是否属于同一部族
            if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny] and grids[nx][ny] == tribe:
                dfs(nx, ny, current_idx)
    
    # 标记所有连通块: 巧妙，一次只标记一个
    for i in range(n):
        for j in range(m):
            if not vis[i][j]:
                dfs(i, j, idx)
                idx += 1
    
    # ans[i]存储第i个连通块周围不同的邻接部族
    ans = [set() for _ in range(idx)]
    
    # 统计每个连通块周围的邻接部族 
    for i in range(n): # 必须把这个 tribe 里的点都检查到，才能确保不漏。
        for j in range(m):
            current_idx = connect[i][j]
            current_tribe = grids[i][j]
            
            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                # 检查边界和是否属于不同部族
                if 0 <= ni < n and 0 <= nj < m and grids[ni][nj] != current_tribe:
                    ans[current_idx].add(grids[ni][nj]) # 不同的就加到set
    
    # 输出结果
    output_lines = []
    for i in range(n):
        line = []
        for j in range(m):
            line.append(str(len(ans[connect[i][j]])))
        output_lines.append(' '.join(line))
    
    sys.stdout.write('\n'.join(output_lines)) #把所有结果按行拼成一个大字符串，一次性输出。用换行符 \n 把 list 里的字符串连起来
if __name__ == "__main__":
    main()