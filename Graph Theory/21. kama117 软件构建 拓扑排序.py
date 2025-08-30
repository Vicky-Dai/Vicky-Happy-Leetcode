# 三个存储结构：记录每个文件的入度、记录结果、记录文件依赖关系
from collections import deque, defaultdict

def topological_sort(n, edges):
    inDegree = [0] * n  #记录每个文件的入度
    umap = defaultdict(list) #记录文件依赖关系 #它创建了一个名为 umap 的字典，其中每个值的默认值是一个空列表 (list)。

    #构建图和入度表
    for s, t in edges:
        inDegree[t] += 1
        umap[s].append(t)

    #初始化队列，加入所有入度为0的节点
    queue = deque([i for i in range(n) if inDegree[i] == 0])
    result = []

    while queue:
        cur = queue.popleft() #当前选中的文件
        result.append(cur)
        for file in umap[cur]: #获取该文件指向的文件
            inDegree[file] -= 1
            if inDegree[file] == 0:
                queue.append(file)
    
    if len(result) == n:
        print(" ".join(map(str, result)))
    else:
        print(-1)

if __name__ == "__main__":
    n, m = map(int, input().split)
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    topological_sort(n, edges)

#与普通字典不同，defaultdict 允许在访问不存在的键时自动生成默认值，而不会引发 KeyError。
#当你使用 defaultdict(list) 时，如果访问字典中一个不存在的键，字典会调用 list() 创建一个新的空列表作为该键的值。