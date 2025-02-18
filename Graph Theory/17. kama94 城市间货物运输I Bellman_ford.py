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