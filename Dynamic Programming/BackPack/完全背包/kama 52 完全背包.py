def test_CompletePack():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagWeight = 4
    dp = [0] * (bagWeight + 1)
    
    for i in range(len(weight)):  # 遍历物品
        print(f"\nConsidering item with weight {weight[i]} and value {value[i]}")
        
        for j in range(weight[i], bagWeight + 1):  # 遍历背包容量
            # 更新 dp[j] 之前，打印当前状态
            print(f"  Before update: dp[{j}] = {dp[j]}")
            
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
            
            # 更新 dp[j] 之后，打印更新后的状态
            print(f"  After update: dp[{j}] = {dp[j]} (using weight {weight[i]})")
        
        # 打印当前 dp 数组的状态
        print("  dp array state:", dp)

test_CompletePack()

#二维数组版本
def test_CompletePack_2D():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagWeight = 4
    num_items = len(weight)
    
    # 初始化 dp 数组，大小为 (num_items + 1) x (bagWeight + 1)，初始值为 0
    dp = [[0] * (bagWeight + 1) for _ in range(num_items + 1)]
    
    # 填充 dp 数组
    for i in range(1, num_items + 1):  # 遍历每个物品
        for j in range(bagWeight + 1):  # 遍历背包容量
            # 如果当前容量 j 小于物品的重量，则不能放入该物品
            if j < weight[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                # 否则，选择放或不放当前物品，取最大值
                dp[i][j] = max(dp[i - 1][j], dp[i][j - weight[i - 1]] + value[i - 1])

            # 打印每一步的 dp 状态（用于查看转移过程）
            print(f"dp[{i}][{j}] = {dp[i][j]}")
    
    # 输出结果，最后一个物品在最大容量下的最大价值
    print("Maximum value:", dp[num_items][bagWeight])

# 运行函数
test_CompletePack_2D()