# 深搜三部曲：1.返回值和参数 2.终止条件 3.单层递归逻辑

#邻接矩阵实现
def dfs(graph, x, n, path, result):
    if x == n:  #当目前遍历的节点 为 最后一个节点 n 的时候 就找到了一条 从出发点到终止点的路径。
        result.append(path.copy()) #创建当前路径 path 的一个浅拷贝。
        return
    for i in range(1, n + 1):
        if graph[x][i] == 1:
            path.append(i)
            dfs(graph, i, n, path, result)
            path.pop() #回溯

def main():
    n, m = map(int, input().split()) #第一行包含两个整数 N，M，表示图中拥有 N 个节点，M 条边
    graph = [[0] * (n + 1) for _ in range(n + 1)]  #邻接矩阵，从节点出发

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


#input() 是一个内置函数，用于从标准输入（通常是键盘）读取一行输入。读取的输入是一个字符串，包含用户输入的所有字符，直到按下回车键为止。
#例如，如果用户输入 4 4 并按下回车键，input() 将返回字符串 '4 4'。
#split() 是 Python 字符串方法之一，用于将字符串按指定的分隔符分割成多个子字符串，并返回一个包含所有子字符串的列表。
#例如，如果用户输入 4 4 并按下回车键，input().split() 将返回列表 ['4', '4']。
#map(int, input().split())：
#map() 函数将列表 ['4', '4'] 中的每个元素应用 int 函数，转换为整数。
#例如，map(int, ['4', '4']) 将返回一个迭代器，其中包含整数 4 和 4。
#n, m = map(int, input().split()) 将迭代器中的两个整数分别赋值给 n 和 m。

#使用pyth.copy()浅拷贝：在深度优先搜索（DFS）中，路径 path 会不断变化。如果直接将 path 添加到 result 中，而不使用 copy，那么 result 中保存的将是 path 的引用，而不是当前路径的一个独立副本。这样，当 path 发生变化时，result 中的路径也会随之变化，导致结果不正确。
#通过使用 path.copy()，我们确保将当前路径的一个独立副本添加到 result 中，这样即使 path 发生变化，result 中的路径也不会受到影响。

#如何分配m n; s t? Python 的 input() 函数每次调用时都会读取一行输入，因此可以确保 n 和 m 从第一行输入中读取，而 s 和 t 从接下来的 m 行输入中读取。

""" __name__ 的作用
当一个 Python 文件被直接运行时，__name__ 的值会被设置为字符串 "__main__"。
当一个 Python 文件被另一个文件导入时，__name__ 的值是该文件的模块名（不包括扩展名 .py）。

通过检查 __name__ == "__main__"，可以控制代码块是否仅在脚本直接运行时执行，而不是在脚本被导入时也执行。 """