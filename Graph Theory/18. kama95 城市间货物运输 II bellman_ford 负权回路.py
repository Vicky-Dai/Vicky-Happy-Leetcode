#这道题和之前的bellman_ford最大的区别就是有了负权回路
#负权回路是指一系列道路的总权值为负，这样的回路使得通过反复经过回路中的道路，理论上可以无限地减少总成本或无限地增加总收益。
#为了避免货物运输商采用负权回路这种情况无限的赚取政府补贴，算法还需检测这种特殊情况。
#如果在这样的图中求最短路的话， 就会在这个环里无限循环 （也是负数+负数 只会越来越小），无法求出最短路径。因为 有负权回路 就是可以无限最短路径（一直绕圈，就可以一直得到无限小的最短距离）。
#那么解决本题的 核心思路，就是在 kama94.城市间货物运输I 的基础上，再多松弛一次，看minDist数组 是否发生变化。

#Bellman_Ford方法
import sys

def main():
    input = sys.stdin.read
    data = input().split()
    index = 0

    n = int(data[index])
    index += 1
    m = int(data[index])
    index += 1

    grid = []
    for i in range(m):
        p1 = int(data[index])
        index += 1
        p2 = int(data[index])
        index += 1
        val = int(data[index])
        index += 1
        grid.append([p1, p2, val]) # p1 指向 p2，权值为 val

    start = 1 
    end = n

    minDist = [float('inf')] * (n+1)
    minDist[start] = 0 # 
    flag = False #

    for i in range(1, n+1): # 这里我们松弛n次，最后一次判断负权回路
        for side in grid:
            from_node = side[0]
            to = side[1]
            price = side[2]
            if i < n:
                if minDist[from_node] != float('inf') and minDist[to] > minDist[from_node] + price:
                    minDist[to] = minDist[from_node] + price
            else: # 多加一次松弛判断负权回路
                if minDist[from_node] != float('inf') and minDist[to] > minDist[from_node] + price:
                    flag = True

    if flag: # 走入了上面的else  flag变为True 说明有负权回路
        print('circle')
    elif minDist[end] == float('inf'):
        print('unconnected')
    else:
        print(minDist[end])

if __name__ == "__main__":
    main()