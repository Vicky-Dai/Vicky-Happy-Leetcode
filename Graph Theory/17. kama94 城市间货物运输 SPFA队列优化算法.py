import collections

def main():
    n, m = map(int, input().strip().split())
    edges = [[] for _ in range(n+1)]
    for _ in range(m):
        src, dest, weight = map(int, input().strip().split())
        edges[src].append([dest, weight]) # 一个for循环接收一行输入

    minDist = [float('inf')] * (n + 1)
    minDist[1] = 0
    que = collections.deque([1])
    visited = [False] * (n+1)
    visited[1] = True #

    while que:
        cur = que.popleft()
        visited[cur] = False #保持只有队列里面的visited是true
        for dest, weight in edges[cur]:
            if minDist[cur] != float('inf') and minDist[cur] + weight < minDist[dest]:
                minDist[dest] = minDist[cur] + weight #更新minDist
                if visited[dest] == False:
                    que.append(dest) # 把更新minDist的节点加入到队列中
                    visited[dest] = True # 对进入队列的元素做记录

    if minDist[-1] == float('inf'):
        return "unconnected"
    return minDist[-1]

if __name__ == "__main__":
    print(main())