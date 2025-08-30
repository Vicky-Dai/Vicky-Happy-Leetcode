class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque, defaultdict
        inDegree = [0] * numCourses
        umap = defaultdict(list)

        for cur, pre in prerequisites:
            inDegree[cur] += 1
            umap[pre].append(cur)

        queue = deque([i for i in range(numCourses) if inDegree[i] == 0])
        while queue:
            c = queue.popleft()
            for co in umap[c]:
                inDegree[co] -= 1
                if inDegree[co] == 0:
                    queue.append(co)
        
        return all(inDegree[i] == 0 for i in range(numCourses))