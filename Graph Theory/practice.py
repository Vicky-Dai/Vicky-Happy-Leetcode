def main():
    n, m = map(int, input().strip().split())
    grid = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e, v = map(int, input().strip().split())
        grid[s].append((e, v))
    minDist = [float('inf')] * (n + 1)
    minDist[1] = 0
    flag = False
    for i in range(1, n+1):
        if i < n:
            for e, v in grid[i]:
                if minDist[i] != float('inf') and minDist[e] > minDist[i] + v:
                    minDist[e] = minDist[i] + v
        else:
            for e, v in grid[i]:
                if minDist[i] != float('inf') and minDist[e] > minDist[i] + v:
                    flag = True
    if flag:
        print('circle')
    elif minDist[n] == float('inf'):
        print('unconnected')
    else:
        print(minDist[n])
if __name__ == "__main__":
    main()
