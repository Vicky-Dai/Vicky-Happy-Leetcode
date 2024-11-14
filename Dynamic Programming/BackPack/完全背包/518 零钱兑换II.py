#和01背包的目标和基本一致
#装满容量j，有dp[j]种方法
#dp[j] += dp[j - coins[i]] 
# 纯完全背包求得装满背包的最大价值是多少，和凑成总和的元素有没有顺序没关系，即：有顺序也行，没有顺序也行！
# 而本题要求凑成总和的组合数，元素之间明确要求没有顺序。本题必须先遍历物品再遍历背包
def change(amount, coins):
    # 创建一个大小为 amount + 1 的 dp 数组，初始化为 0
    dp = [0] * (amount + 1)
    # 金额为 0 时，只有一种组合方式，即不使用任何硬币
    dp[0] = 1

    # 遍历每个硬币
    for coin in coins:
        # 从 coin 到 amount 遍历，更新每个金额的组合数
        for j in range(coin, amount + 1):
            dp[j] += dp[j - coin]
            print(f"使用硬币 {coin} 更新 dp[{j}] 为 {dp[j]}")

    # dp[amount] 即为能组成金额 amount 的组合数
    return dp[amount]

# 示例
coins = [1, 2, 5]  # 硬币面额
amount = 5          # 目标金额

result = change(amount, coins)
print("组成目标金额的硬币组合数:", result)

print("----------------------------------")

def change(amount, coins):
    # 创建一个大小为 amount + 1 的 dp 数组，初始化为 0
    dp = [0] * (amount + 1)
    # 金额为 0 时，只有一种组合方式，即不使用任何硬币
    dp[0] = 1

    # 遍历每个硬币
    for j in range(0, amount + 1):
        # 从 coin 到 amount 遍历，更新每个金额的组合数
        for coin in coins:
            dp[j] += dp[j - coin]
            print(f"使用硬币 {coin} 更新 dp[{j}] 为 {dp[j]}")

    # dp[amount] 即为能组成金额 amount 的组合数
    return dp[amount]

# 示例
coins = [1, 2, 5]  # 硬币面额
amount = 5          # 目标金额

result = change(amount, coins)
print("组成目标金额的硬币组合数:", result)

#充分证明了，后者是错的，前者是组合后者是排列，本道题要求的是组合，这是为什么会这样呢？因为后者不断地用125更新，之前放过2，后面还可能再放1，所以就会有12 和21 但是其实在组合看来这两者是一样的