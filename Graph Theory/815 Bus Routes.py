from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        n = len(routes)
        edge = [[False] * n for _ in range(n)]
        rec = defaultdict(list)

        # 建图：找出哪些公交线路相互连接（有相同站点）
        for i in range(n):
            for site in routes[i]:
                for j in rec[site]:
                    edge[i][j] = edge[j][i] = True
                rec[site].append(i)

        dis = [-1] * n
        que = deque()

        # 初始化：从 source 出发的公交线路入队
        for bus in rec[source]:
            dis[bus] = 1
            que.append(bus)

        # BFS 计算最少换乘次数
        while que:
            x = que.popleft()
            for y in range(n):
                if edge[x][y] and dis[y] == -1:
                    dis[y] = dis[x] + 1
                    que.append(y)

        ret = float('inf')
        for bus in rec[target]:
            if dis[bus] != -1:
                ret = min(ret, dis[bus])

        return -1 if ret == float('inf') else ret
