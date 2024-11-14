#brute force 回溯 O(2^n) n是物品数量，因为每个物品只有0和1两种状态

n, bagweight = map(int, input().split())  #map(function, iterable) map对刻碟带对象的每个元素进行指定函数的操作，int在python里也是一种函数，转换格式函数
#input().split()是字符串的方法，作用是将字符串按空白字符（空格、制表符等）分割成一个字符串列表。
weight = list(map(int, input().split()))
value = list(map(int, input().split()))

dp = [[0] * (bagweight + 1) for _ in range(n)] #创建一个二维数组，用于求解

for j in range(weight[0], bagweight + 1): #初始化，如果背包的容量大于第一个物品的重量，就初始化为第一个物品重量（因为目前只有第一个物品），固定在第一行（物品），遍历列（背包容量）
    dp[0][j] = value[0]

for i in range(1, n):  #这道题先遍历背包和物品都可以，因为都取决于上方和左上方的结果，但是不是所有题都这样
    for j in range(bagweight + 1):
        if j < weight[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])

# 对于每个物品 i 和每个背包容量 j：
# 如果当前背包容量 j 小于物品 i 的重量 weight[i]，则无法放入该物品，dp[i][j] 直接等于不放入该物品时的最大价值 dp[i - 1][j]。
# 如果 j 大于或等于 weight[i]，则有两种选择：
# 不放入物品 i，此时的价值为 dp[i - 1][j]。
# 放入物品 i，此时的价值为 dp[i - 1][j - weight[i]] + value[i]。
# dp[i][j] 取两者的最大值，以确保当前背包容量下获得最大的价值。


print(dp[n - 1][bagweight])


#画图看图很重要