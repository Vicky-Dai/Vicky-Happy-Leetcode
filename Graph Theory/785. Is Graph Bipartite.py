class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # think of 886
        # go through each edge, we find the two nodes
        # the two connected nodes should be diffrent colour
        # so
        # loop through the edges
        # dfs each node give color and judge if they meet the standard
        n = len(graph) # 4  [[1,2,3],[0,2],[0,1,3],[0,2]]
        color = [0]*n # 

        # color = [1, -1, 1, 0]
        def dfs(node, c):
            if color[node] != 0:       # 已上色
                return color[node] == c  # 必须颜色一致
            color[node] = c
            for v in graph[node]:
                if not dfs(v, -c):
                    return False
            return True
        
        for i in range(n): # 0
            if color[i] == 0:
                if not dfs(i, 1):
                    return False
        return True


# Recursion in Graph, be careful about the infinite loop
        def dfs(node, c): # dfs(2, -1)  # [0, 1, 3]
            if color[node] == 0: 
                color[node] = c 
            if color[node] == -c: # c=-1  -c=1 color[2] == 1 == 1 return False
                return False
            for v in graph[node]: 
                if not dfs(v, -c):  
                    return False
            return True