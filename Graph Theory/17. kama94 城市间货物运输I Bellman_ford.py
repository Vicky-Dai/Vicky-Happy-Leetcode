def main():
    n, m = map(int, input().strip().split())
    edges = []
    for _ in range(m):
        src, dest, weight = map(int, input().strip().split())
        edges.append([src, dest, weight])

    minDist = [float('inf')] * (n+1)
    minDist[1] = 0

    for i in range(1, n):
        updated = False
        for src, dest, weight in edges:
            if minDist[src] != float('inf') and minDist[src] + weight < minDist[dest]: 
                minDist[dest] = minDist[src] + weight
                updated = True
        if not updated: # 若边不再更新，即停止回圈
            break
    if minDist[-1] == float("inf"):
        return "unconnected"
    return minDist[-1]

if __name__ == "__main__":
    print(main())


# 我自己写的
def main():    
    n, m = map(int, input().split())
    minDist = [float('inf')] * (n + 1)
    minDist[1] = 0  # 起点到自己的距离为0 你应该把起点（通常是1号点）的距离初始化为0，否则所有点的距离都是 inf，算法无法更新
    edges = []
    for _ in range(m):
        s, e, v = map(int, input().split())
        edges.append((s, e, v))
    for i in range(1, n):
        for s, e, v in edges:
            if minDist[s] != float('inf'): # ！！！！ 这个点已经可以到达时，才尝试用它去松弛（更新）其它点的距离。
                minDist[e] = min(minDist[e], minDist[s] + v)
    if minDist[n] == float('inf'):
        print("unconnected")
    else:
        print(minDist[n])
if __name__ == "__main__":
    main()
