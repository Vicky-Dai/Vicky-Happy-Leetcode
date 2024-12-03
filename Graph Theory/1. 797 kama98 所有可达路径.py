# 深搜三部曲：1.返回值和参数 2.终止条件 3.单层递归逻辑

def dfs(graph, x, n, path, result):
    if x == n:  #当目前遍历的节点 为 最后一个节点 n 的时候 就找到了一条 从出发点到终止点的路径。
        result.append(path.copy())
        return
    for i in range(1, n + 1):
        if graph[x][i] == 1:
            path.append(i)
            dfs(graph, i, n, path, result)
            path.pop() #回溯

def main():
    n, m = map(int, input().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)] 

    for _ in range(m):
        s, t = map(int, input().split())
        graph[s][t] = 1

    result = []
    dfs(graph, 1, n, [1], result)

    if not result:
        print(-1)
    else:
        for path in result:
            print(' '.join(map(str, path))) #.join() 是 Python 字符串方法之一，用于将可迭代对象中的元素连接成一个字符串，并在每个元素之间插入指定的分隔符。

if __name__ == "__main__":
    main()