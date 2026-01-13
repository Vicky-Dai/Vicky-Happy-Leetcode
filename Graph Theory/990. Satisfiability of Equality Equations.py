# 并查集用来管理元素之间的等价关系（连通性判断）
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # equations[i] x1 y1
        # True False -> assign integers to variable names
        parent = list(range(26))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        # 1️⃣ 先处理所有相等关系
        for e in equations:
            if e[1] == '=':
                a = ord(e[0]) - ord('a')
                b = ord(e[3]) - ord('a')
                union(a, b)
        
        # 2️⃣ 再检查所有不等关系是否冲突
        for e in equations:
            if e[1] == '!':
                a = ord(e[0]) - ord('a')
                b = ord(e[3]) - ord('a')
                if find(a) == find(b):
                    return False
        
        return True      