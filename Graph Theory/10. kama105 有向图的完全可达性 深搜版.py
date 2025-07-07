def dfs(graph, key, visited):
    for neighbor in graph[key]:
        if not visited[neighbor]:
            visited[neighbor] = True
            dfs(graph, neighbor, visited)

def main():
    import sys
    input = sys.stdin.read #  从标准输入读取数据。
    data = input().split()

    n = int(data[0])
    m = int(data[1])

    graph = [[] for _ in range(n+1)]
    index = 2
    for _ in range(m):
        s = int(data[index])
        t = int(data[index + 1])
        graph[s].append(t)
        index += 2

    visited = [False] * (n + 1)
    visited[1] = True
    dfs(graph, 1, visited)

    for i in range(1, n + 1):
        if not visited[i]:
            print(-1)
            return
        
    print(1)

if __name__ == "__main__":
    main()


# 我自己写的版本 
def dfs(grid, key, visited):
    for i, p in enumerate(grid[key]):
        if not visited[p]:
            visited[p] = True
            dfs(grid, p, visited)


def main():
    n, k = map(int, input().split())
    visited = [False] * (n+1)
    visited[1] = True
    grid = [[] for _ in range(n+1)]
    for _ in range(k):
        s, e = map(int, input().split())
        grid[s].append(e)
    dfs(grid, 1, visited)

    for i in range(1, n+1):
        if not visited[i]:
            print('-1')
            return
    print('1') 

if __name__ == "__main__":
    main()

