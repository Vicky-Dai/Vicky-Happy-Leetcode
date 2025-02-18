#本题为单源有限最短路问题
#本题是 kama94.城市间货物运输I 的拓展题，bellman_ford 标准写法是松弛 n-1 次，本题就松弛 k + 1次就好。
#本题是最多经过 k 个城市， 那么是 k + 1条边相连的节点。
#时间复杂度： O(K * E) , K为至多经过K个节点，E为图中边的数量
#空间复杂度： O(N) ，即 minDist 数组所开辟的空间

def main():
    # 輸入
    n, m = map(int, input().split())
    edges = list()
    for _ in range(m):
        edges.append(list(map(int, input().split() )))
    
    start, end, k = map(int, input().split())
    min_dist = [float('inf') for _ in range(n + 1)]
    min_dist[start] = 0
    
    # 只能經過k個城市，所以從起始點到中間有(k + 1)個邊連接
    # 需要鬆弛(k + 1)次
    
    for _ in range(k + 1):
        update = False
        min_dist_copy = min_dist.copy()
        for src, desc, w in edges:
            if (min_dist_copy[src] != float('inf') and 
            min_dist_copy[src] + w < min_dist[desc]):
                min_dist[desc] = min_dist_copy[src] + w
                update = True
        if not update:
            break
    # 輸出
    if min_dist[end] == float('inf'):
        print('unreachable')
    else:
        print(min_dist[end])
            
            

if __name__ == "__main__":
    main()