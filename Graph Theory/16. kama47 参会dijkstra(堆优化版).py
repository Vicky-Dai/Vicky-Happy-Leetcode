import heapq

class Edge:  # convenient to record the edge destination and its value
    def __init__(self, to, val):
        self.to = to
        self.val = val

def dijkstra(n, m, edges, start, end):
    grid = [[] for _ in range(n+1)]

    for p1, p2, val in edges:
        grid[p1].append(Edge(p2, val))

    minDist = [float('inf')] * (n+1) #!!!!!!!!! initialize the distance array with infinity
    visited = [False] * (n+1)

    pq = []
    heapq.heappush(pq, (0, start))
    minDist[start] = 0 # !!!!!!!!!! remember this!

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)

        if visited[cur_node]: # !!!!!!!!!don't forget to pass the visited one
            continue
        visited[cur_node] = True #找到距离最近的node，并且标为visited

        for edge in grid[cur_node]:
            if not visited[edge.to] and cur_dist + edge.val < minDist[edge.to]:
#!visited[edge.to] ， 目前 源点到cur.first的最短距离（minDist） + cur.first 到 edge.to 的距离 （edge.val） 是否 小于 minDist已经记录的 源点到 edge.to 的距离 （minDist[edge.to]）
                minDist[edge.to] = cur_dist + edge.val
                heapq.heappush(pq, (minDist[edge.to], edge.to))
    return -1 if minDist[end] == float('inf') else minDist[end]

#输入