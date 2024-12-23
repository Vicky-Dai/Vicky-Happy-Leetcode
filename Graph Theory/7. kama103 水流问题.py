first = set()
second = set()
directions = [[-1,0], [0,1], [1,0], [0,-1]]

def dfs(i, j, graph, visited, side):
    if visited[i][j]:
        return
    
    visited[i][j] = True
    side.add((i,j))

    for x,y in directions:
        new_x = i + x
        new_y = j + y
        if (
            0 <= new_x < len(graph)
            and 0 <= new_y < len(graph[0])
            and int(graph[new_x][new_y] >= int(graph[i][j])) #判断一下是不是比之前的地方高
        ):
            dfs(new_x, new_y, graph, visited, side)
        
def main():
    global first
    global seconde

    N, M = map(int, input().strip().split())
    graph = []
    for _ in range(N):
        row = input().strip().split()
        graph.append(row)

    #是否可以到达第一边界
    visited = [[False]*M for _ in range(N)]
    for i in range(M):
        dfs(0, i, graph, visited, first) #上
    for i in range(N):
        dfs(i, 0, graph, visited, first) #左

    #是否可以到达第二边界
    visited = [[False]*M for _ in range(N)]
    for i in range(M):
        dfs(N - 1, i, graph, visited, second) #下
    for i in range(N):
        dfs(i, M - 1, graph, visited, second) # 右

    # 可到达第一边界和第二边界
    res = first & second
    #这是一个按位与运算符（&）。它将两个操作数的每一位进行比较，如果两个对应的位都是 1，则结果为 1，否则结果为 0。

    for x,y in res:
        print(f"{x} {y}") #这是一个 f-string（格式化字符串），用于将变量的值嵌入到字符串中 中间打空格就会输出空字符串，把xy分开

if __name__ == "__main__":
    main()
