#本题的本质是 ：有一个有向图，是由一颗有向树 + 一条有向边组成的 （所以此时这个图就不能称之为有向树），现在让我们找到那条边 把这条边删了，让这个图恢复为有向树。
#两种大的情况 入度为 2 的情况和直接存在环的情况，本质上是两种不同的多余边情况。

from collections import defaultdict

father = list()

def find(u):
    if u == father[u]:
        return u
    else:
        father[u] = find(father[u])
        return father[u]
    
def is_same(u, v):
    u = find(u)
    v = find(v)
    return u == v
    
    
def join(u, v):
    u = find(u)
    v = find(v)
    if u != v:
        father[u] = v
    
    
def is_tree_after_remove_edge(edges, edge, n):
    # 初始化并查集
    global father 
    father = [i for i in range(n + 1)]
    
    for i in range(len(edges)):
        if i == edge:
            continue
        s, t = edges[i]
        if is_same(s, t): # 成環，即不是有向樹
            return False
        else: # 將s,t放入集合中
            join(s, t)
    return True
    

def get_remove_edge(edges):
    # 初始化并查集
    global father
    father = [i for i in range(n + 1)]
    
    for s, t in edges:
        if is_same(s, t):
            print(s, t)
            return
        else:
            join(s, t)
        

if __name__ == "__main__":
    # 輸入
    n = int(input())
    edges = list()
    in_degree = defaultdict(int)
    
    for i in range(n):
        s, t = map(int, input().split())
        in_degree[t] += 1
        edges.append([s, t])
        
    # 尋找入度為2的邊，並紀錄其下標(index)
    vec = list()
    for i in range(n - 1, -1, -1): # 逆序遍历原因，下面有写
        if in_degree[edges[i][1]] == 2:
            vec.append(i)       # 这里没太看明白？？？
            
    # 輸出
    if len(vec) > 0:
        # 情況一：刪除輸出順序靠後的邊 
        if is_tree_after_remove_edge(edges, vec[0], n):
            print(edges[vec[0]][0], edges[vec[0]][1])
        # 情況二：只能刪除特定的邊
        else:
            print(edges[vec[1]][0], edges[vec[1]][1])
    else:
        # 情況三： 原圖有環
        get_remove_edge(edges)
        #如果没有节点入度为 2，则说明图中直接存在环。调用 get_remove_edge 来找到环中形成的边。

#逆序遍历的原因是，我们通常想保留更早加入的边，而删除更晚加入的边，符合"尽可能少破坏树结构"的原则。