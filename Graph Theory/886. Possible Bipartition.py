class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        color = [0] * (n + 1)  # 0 = uncolored, 1 = red, -1 = blue

        def dfs(node, c):
            color[node] = c
            for nei in graph[node]:
                if color[nei] == c: # 如果相邻节点颜色相同，返回 False
                    return False
                if color[nei] == 0 and not dfs(nei, -c): # 如果相邻节点未染色，染相反颜色
                    return False
            return True

        for i in range(1, n + 1):
            if color[i] == 0:      # 若是新连通块
                if not dfs(i, 1):  # 任意颜色开始染
                    return False

        return True
