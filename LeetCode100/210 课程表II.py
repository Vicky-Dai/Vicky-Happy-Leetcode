class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0] * numCourses
        umap = defaultdict(list)

        for s, t in prerequisites:
            inDegree[t] += 1
            umap[s].append(t)
        
        queue = deque([i for i in range(numCourses) if inDegree[i] == 0])
        visited = 0

        while queue:
            visited += 1
            cur = queue.popleft()
            for course in umap[cur]:
                inDegree[course] -= 1
                if inDegree[course] == 0:
                    queue.append(course)
        
        return visited == numCourses
            