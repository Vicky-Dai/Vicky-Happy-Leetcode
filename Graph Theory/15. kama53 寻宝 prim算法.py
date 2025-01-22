#接收输入
v, e = list(map(int, input().strip().split()))
#按照常规的邻接矩阵存储图信息，不可达的初始化为10001
graph = [[10001] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    x, y, w = list(map(int, input().strip().split()))
    graph[x][y] = w
    graph[y][x] = w #因为是一个无向图

#定义加入生成树的标记数组和未加入生成树的最近距离minDist
visited = [False] * (v+1)
minDist = [10001] * (v+1)
#parent = [-1] * (v+1)

#循环n-1次，建立n-1条边
#从节点视角来看： 没选中一个节点加入树（visted), 更新剩余节点到生成树的最短距离（minDist
#这一步其实蕴含了确定下一条选取的边，计入总路程ans的计算（prim三部曲第三步）
for _ in range(1, v+1):
    min_val = 10002
    cur = -1
    """ 第一步，选取距离生成树最近的节点 """
    for j in range(1, v+1): #依次遍历点
        if visited[j] == False and minDist[j] < min_val: 
            cur = j 
            min_minval = minDist[j] #循环比较 找到距离生成树最近的
    visited[cur] = True #完成第一步，选取并标记为true
    """ 第二步，最近节点加入生成树 """
    for j in range(1, v+1): #第二部，最近
        if visited[j] == False and minDist[j] > graph[cur][j]:
            minDist[j] = graph[cur][j] 
            # parent[j] = cur; // 记录边
    
# for j in range(1, v+1):
#     print(f"{i}->{parent[i]}")
ans = 0
for i in range(2, v + 1):
    ans += minDist[i]
print(ans)
