class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        inDegree = [0] * numCourses
        umap = defaultdict(list)
        for cur, pre in prerequisites:
            inDegree[cur] += 1
            umap[pre].append(cur)  # ！！！！pre -> cur, 也就是 pre 先修，cur 后修 注意建图的方向
        q = deque([i for i in range(numCourses) if inDegree[i] == 0])
        
        res = []

        
        while q:
            i = q.popleft()
            res.append(i)
            for k in umap[i]:
                inDegree[k] -= 1
                if inDegree[k] == 0:
                    q.append(k)
        return res if all(inDegree[i] == 0 for i in range(numCourses)) else []  #！！！！！！！ 注意 有环没环