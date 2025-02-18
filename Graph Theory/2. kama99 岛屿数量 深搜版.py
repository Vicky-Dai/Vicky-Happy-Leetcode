#岛屿问题，这类问题的特征就是不涉及具体的遍历方式，只要能把相邻且相同属性的节点标记上就行。 这类问题深搜广搜都可以
#本题思路:遇到一个没有遍历过的节点陆地，计数器就加一，然后把该节点陆地所能遍历到的陆地都标记上。
#再遇到标记过的陆地节点和海洋节点的时候直接跳过。 这样计数器就是最终岛屿的数量。
#版本二 ：dfs有终止条件

direction = [[0,1], [1, 0], [0, -1], [-1, 0]] #四个方向：上下左右
def dfs(grid, visited, x, y):
    """ 对陆地进行深度优先遍历并且标记 """
    #和版本一的区别是在调用前增加判断终止条件
    if visited[x][y] or grid[x][y] == 0: #如果已经访问过或者是海洋，就直接退出不标记
        return 
    visited[x][y] = True

    for i, j in direction:
        next_x = x + i
        next_y = y + j
        if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]): #下标越界，太小，或者超出长度 注意等于长度也是超出（数组下标）
            continue
        dfs(grid, visited, next_x, next_y) #由于递归条件判断放在了方法首部，直接使用dfs方法

if __name__ == "__main__":
    n, m = map(int, input().split())

    #邻接矩阵
    grid = []
    for _ in range(n): #行
        grid.append(list(map(int, input().split()))) #列 实际上就是一个二维数组，每一行是一个一维数组

    visited = [[False] * m for _ in range(n)] #访问表，用于标记是否访问过

    res = 0
    for i in range(n):
        for j in range(m):
            #判断，如果当前节点是陆地 并且没有访问过，res+1并标记访问该节点，再使用深度搜索标记相邻陆地
            if grid[i][j] == 1 and not visited[i][j]:
                res += 1
                dfs(grid, visited, i, j)
    print(res)


#if __name__ == "__main__": 用于确保 main() 函数只有在直接运行脚本时才会执行。如果将该脚本作为模块导入到其他脚本中，main() 函数不会执行。
#例如在别的文件import这个文件，这个文件的main()就不会执行，否则会出错一直执行