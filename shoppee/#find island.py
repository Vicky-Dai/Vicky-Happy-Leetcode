#find island bfs
from collections import deque

class Solution:
    def apply(self, generated_map):
        n = len(generated_map)
        visited = [[False for _ in range(n)] for _ in range(n)]
        queue = deque()
        queue.append((0, 0))
        visited[0][0] = True
        
        # 定义四个方向的移动
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # 检查新坐标是否合法且未被访问，且是可行区域
                if 0 <= nx < n and 0 <= ny < n:
                    if not visited[nx][ny] and generated_map[nx][ny] == 0:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
        
        # 统计原生障碍的数量
        count_ones = sum(row.count(1) for row in generated_map) # count可以统计数量
        # 统计不可达的 0 的数量
        count_unreachable_zero = 0
        for i in range(n):
            for j in range(n):
                if generated_map[i][j] == 0 and not visited[i][j]:
                    count_unreachable_zero += 1
        
        return count_ones + count_unreachable_zero

#dfs
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 四个方向：上、下、左、右

def dfs(generated_map, visited, x, y):
    """ 深度优先遍历可达区域并标记访问 """
    if visited[x][y] or generated_map[x][y] == 1: # 已访问或是障碍物，直接返回
        return 
    visited[x][y] = True
    
    for dx, dy in direction:
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < len(generated_map) and 0 <= next_y < len(generated_map[0]): # 边界检查
            dfs(generated_map, visited, next_x, next_y)

if __name__ == "__main__":
    n = int(input())
    
    # 读取地图
    generated_map = [list(map(int, input().split())) for _ in range(n)]
    
    visited = [[False] * n for _ in range(n)] # 访问标记
    
    # 从 (0, 0) 开始标记可达区域
    dfs(generated_map, visited, 0, 0)
    
    # 统计原生障碍的数量
    count_ones = sum(row.count(1) for row in generated_map)
    
    # 统计不可达的 0 的数量
    count_unreachable_zero = sum(1 for i in range(n) for j in range(n) if generated_map[i][j] == 0 and not visited[i][j]) #只要条件满足就生成一个1
    
    print(count_ones + count_unreachable_zero)
