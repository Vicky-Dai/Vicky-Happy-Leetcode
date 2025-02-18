n, bagweight = map(int, input().split())

weight = list(map(int, input().split()))
value = list(map(int, input().split()))

dp = [[0] * (bagweight + 1) for _ in range(n)]

for j in range(weight[0], bagweight + 1):
    dp[0][j] = value[0]

for i in range(1, n):
    for j in range(bagweight + 1):
        if j < weight[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])

print(dp[n - 1][bagweight])


def knapsack(weights, values, capacity):
    n = len(values)
    
    # 创建一维数组 dp，用于保存每个容量下的最大价值
    dp = [0] * (capacity + 1)

    # 打印初始状态
    print("初始状态:", dp)

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):  # 从后往前遍历
            # 更新 dp[w]，选择当前物品或不选择
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
        
        # 打印每次物品添加后的状态
        print(f"添加物品 {i + 1} (重量: {weights[i]}, 价值: {values[i]}) 后状态:", dp)

    return dp[capacity]

# 示例
weights = [2, 3, 4, 5]  # 物品的重量
values = [3, 4, 5, 6]   # 物品的价值
capacity = 5             # 背包的最大容量

max_value = knapsack(weights, values, capacity)
print("最大价值:", max_value)

print("----------------------------------")

def knapsack(weights, values, capacity):
    n = len(values)
    
    # 创建一个二维数组 dp，初始化为 0
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # 打印初始状态
    print("初始状态:")
    for row in dp:
        print(row)

    # 动态规划填充 dp 数组
    for i in range(1, n + 1):  # 物品从 1 开始
        for w in range(capacity + 1):  # 容量从 0 到 capacity
            if weights[i - 1] <= w:
                # 可以选择当前物品
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # 不能选择当前物品
                dp[i][w] = dp[i - 1][w]
        
        # 打印每次物品添加后的状态
        print(f"添加物品 {i} (重量: {weights[i - 1]}, 价值: {values[i - 1]}) 后状态:")
        for row in dp:
            print(row)

    return dp[n][capacity]

# 示例
weights = [2, 3, 4, 5]  # 物品的重量
values = [3, 4, 5, 6]   # 物品的价值
capacity = 5             # 背包的最大容量

max_value = knapsack(weights, values, capacity)
print("最大价值:", max_value)