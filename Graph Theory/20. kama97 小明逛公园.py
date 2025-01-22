#Floyd算法
#本题是经典的多源最短路问题。
#时间复杂度： O(n^3)
#空间复杂度：O(n^2)
#这里我们用 grid数组来存图，那就把dp数组命名为 grid。
#grid[i][j][k] = m，表示 节点i 到 节点j 以[1...k] 集合中的一个节点为中间节点的最短距离为m。

#基于三维数组的Floyd 更容易理解，注重遍历顺序理解
if __name__ == '__main__':
    max_int = 10005 #设置最大路径，因为边最大距离为10^4
    n, m = map(int, input().split())
    grid = [[[max_int]*(n+1) for _ in range(n+1)] for _ in range(n+1)] #初始化三维dp数组

    for _ in range(m):
        p1, p2, w = map(int, input().split())
        grid[p1][p2][0] = w
        grid[p2][p1][0] = w

    #开始floyd
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                grid[i][j][k] = min(grid[i][j][k-1], grid[i][k][k-1] + grid[k][j][k-1])

    #输出结果
    z = int(input())
    for _ in range(z):
        start, end = map(int, input().split())
        if grid[start][end][n] == max_int:
            print(-1)
        else:
            print(grid[start][end][n])

#二维数组版
if __name__ == '__main__':
    max_int = 10005  # 设置最大路径，因为边最大距离为10^4

    n, m = map(int, input().split())

    grid = [[max_int]*(n+1) for _ in range(n+1)]  # 初始化二维dp数组

    for _ in range(m):
        p1, p2, val = map(int, input().split())
        grid[p1][p2] = val
        grid[p2][p1] = val

    # 开始floyd
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])

    # 输出结果
    z = int(input())
    for _ in range(z):
        start, end = map(int, input().split())
        if grid[start][end] == max_int:
            print(-1)
        else:
            print(grid[start][end])