def main():    
    n, m = map(int, input().split())
    minDist = [float('inf')] * (n + 1)
    minDist[1] = 0  # 起点到自己的距离为0
    edges = []
    for _ in range(m):
        s, e, v = map(int, input().split())
        edges.append((s, e, v))
    for i in range(1, n):
        for s, e, v in edges:
            if minDist[s] != float('inf'):
                minDist[e] = min(minDist[e], minDist[s] + v)
    if minDist[n] == float('inf'):
        print("unconnected")
    else:
        print(minDist[n])
if __name__ == "__main__":
    main()
