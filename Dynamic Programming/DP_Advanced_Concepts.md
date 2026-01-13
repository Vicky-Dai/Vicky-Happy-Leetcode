# 动态规划高级概念详解

## 1. 状态压缩详解

### 什么是状态压缩？

**状态压缩**是指通过减少DP数组的维度来优化空间复杂度，通常是将二维或高维数组压缩为一维数组，或者用更紧凑的方式表示状态。

### 为什么需要状态压缩？

#### 1. **空间优化**
- 减少内存使用
- 提高缓存效率
- 避免内存溢出

#### 2. **性能提升**
- 减少数组访问开销
- 提高代码执行效率

### 状态压缩的常见类型

#### 1. **滚动数组优化**

**原始版本（二维数组）：**
```python
# 斐波那契数列 - 二维版本
def fib_2d(n):
    if n <= 1:
        return n
    
    dp = [[0] * 2 for _ in range(n + 1)]
    dp[0][0] = 0
    dp[0][1] = 1
    
    for i in range(1, n + 1):
        dp[i][0] = dp[i-1][1]  # 前一个数
        dp[i][1] = dp[i-1][0] + dp[i-1][1]  # 当前数
    
    return dp[n][1]
```

**状态压缩版本（一维数组）：**
```python
# 斐波那契数列 - 状态压缩版本
def fib_compressed(n):
    if n <= 1:
        return n
    
    # 只需要保存前两个值
    prev2, prev1 = 0, 1
    
    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1  # 更新前两个值
        prev1 = curr
    
    return prev1
```

#### 2. **背包问题的状态压缩**

**原始版本（二维数组）：**
```python
# 01背包 - 二维版本
def knapsack_2d(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(capacity + 1):
            if j >= weights[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][capacity]
```

**状态压缩版本（一维数组）：**
```python
# 01背包 - 状态压缩版本
def knapsack_compressed(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        # 从后往前遍历，避免覆盖
        for j in range(capacity, weights[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    
    return dp[capacity]
```

#### 3. **位运算状态压缩**

**问题：** 旅行商问题（TSP）
```python
# 使用位运算表示访问过的城市
def tsp_bitmask(dist):
    n = len(dist)
    # dp[mask][i] 表示访问过mask中的城市，当前在城市i的最小代价
    dp = [[float('inf')] * n for _ in range(1 << n)]
    
    # 初始化：从城市0开始
    dp[1][0] = 0
    
    for mask in range(1 << n):
        for i in range(n):
            if not (mask & (1 << i)):  # 城市i未被访问
                continue
            for j in range(n):
                if mask & (1 << j):  # 城市j已被访问
                    continue
                # 从城市i到城市j
                dp[mask | (1 << j)][j] = min(
                    dp[mask | (1 << j)][j],
                    dp[mask][i] + dist[i][j]
                )
    
    # 返回访问所有城市后回到起点的最小代价
    return min(dp[(1 << n) - 1][i] + dist[i][0] for i in range(1, n))
```

### 状态压缩的关键技巧

#### 1. **滚动数组**
```python
# 最大子数组和 - 状态压缩
def maxSubArray_compressed(nums):
    prev = nums[0]
    result = prev
    
    for i in range(1, len(nums)):
        curr = max(nums[i], prev + nums[i])
        result = max(result, curr)
        prev = curr  # 更新前一个状态
    
    return result
```

#### 2. **空间换时间**
```python
# 爬楼梯 - 状态压缩
def climbStairs_compressed(n):
    if n <= 2:
        return n
    
    prev2, prev1 = 1, 2
    
    for i in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    
    return prev1
```

#### 3. **位运算优化**
```python
# 使用位运算表示状态
def bitmask_example():
    # 用二进制位表示状态
    state = 0b1010  # 表示第1和第3个位置被选中
    
    # 检查第i位是否被选中
    def is_set(state, i):
        return (state >> i) & 1
    
    # 设置第i位
    def set_bit(state, i):
        return state | (1 << i)
    
    # 清除第i位
    def clear_bit(state, i):
        return state & ~(1 << i)
```

### 状态压缩的注意事项

#### 1. **遍历顺序**
```python
# 01背包必须从后往前遍历
for j in range(capacity, weights[i] - 1, -1):
    dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

# 完全背包可以从前往后遍历
for j in range(weights[i], capacity + 1):
    dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
```

#### 2. **状态依赖**
```python
# 确保状态更新时，依赖的状态没有被覆盖
# 错误示例：
for i in range(n):
    for j in range(capacity + 1):  # 从前往后会覆盖
        dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

# 正确示例：
for i in range(n):
    for j in range(capacity, weights[i] - 1, -1):  # 从后往前
        dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
```

---

## 2. 线性DP详解

### 什么是线性DP？

**线性DP**是指状态转移只依赖于**前一个或前几个状态**的DP问题，状态之间呈线性关系，通常用一维数组来存储状态。

### 线性DP的特征

#### 1. **状态定义**
```python
# 通常用一维数组
dp[i] 表示以第i个位置结尾的某种状态
```

#### 2. **状态转移**
```python
# 状态转移通常只依赖前一个或前几个状态
dp[i] = f(dp[i-1], dp[i-2], ..., dp[i-k])
```

#### 3. **遍历顺序**
```python
# 通常从前往后遍历
for i in range(1, n):
    dp[i] = ...
```

### 线性DP的经典例子

#### 1. **斐波那契数列**
```python
class Solution:
    def fib(self, n: int) -> int:
        # dp[i] 表示第i个斐波那契数
        if n <= 1:
            return n
        
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        
        # 线性转移：dp[i] = dp[i-1] + dp[i-2]
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
```

#### 2. **爬楼梯问题**
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] 表示爬到第i阶的方法数
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        # 线性转移：dp[i] = dp[i-1] + dp[i-2]
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
```

#### 3. **最大子数组和**
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] 表示以nums[i]结尾的最大子数组和
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        result = dp[0]
        
        # 线性转移：dp[i] = max(nums[i], dp[i-1] + nums[i])
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            result = max(result, dp[i])
        
        return result
```

#### 4. **打家劫舍**
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] 表示偷到第i个房屋时的最大金额
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # 线性转移：dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[n-1]
```

### 线性DP的状态转移模式

#### 1. **依赖前一个状态**
```python
# 如：最大子数组和
dp[i] = max(nums[i], dp[i-1] + nums[i])
```

#### 2. **依赖前两个状态**
```python
# 如：斐波那契数列、爬楼梯
dp[i] = dp[i-1] + dp[i-2]
```

#### 3. **依赖前k个状态**
```python
# 如：k步爬楼梯
dp[i] = dp[i-1] + dp[i-2] + ... + dp[i-k]
```

### 线性DP vs 其他DP类型

#### 对比表格：

| 特征 | 线性DP | 背包DP | 子序列DP | 矩阵DP |
|------|--------|--------|----------|--------|
| **状态维度** | 一维 | 一维/二维 | 二维 | 二维 |
| **状态依赖** | 前几个状态 | 容量+物品 | 两个序列 | 上下左右 |
| **遍历方式** | 从前往后 | 特殊顺序 | 两层循环 | 行列遍历 |
| **典型问题** | 斐波那契、爬楼梯 | 01背包、完全背包 | LCS、LIS | 路径问题 |

### 线性DP的解题步骤

#### 1. **确定状态定义**
```python
# 问自己：dp[i]表示什么？
dp[i] = 以第i个位置结尾的某种状态
```

#### 2. **找出状态转移方程**
```python
# 问自己：dp[i]如何从之前的状态得到？
dp[i] = f(dp[i-1], dp[i-2], ..., dp[i-k])
```

#### 3. **确定初始状态**
```python
# 问自己：dp[0], dp[1]等初始值是什么？
dp[0] = ...
dp[1] = ...
```

#### 4. **确定遍历顺序**
```python
# 问自己：需要从前往后还是从后往前？
for i in range(1, n):  # 通常从前往后
    dp[i] = ...
```

#### 5. **考虑空间优化**
```python
# 问自己：能否用滚动数组优化？
prev2, prev1 = 0, 1
for i in range(2, n + 1):
    curr = prev1 + prev2
    prev2 = prev1
    prev1 = curr
```

### 线性DP的常见变种

#### 1. **单状态线性DP**
```python
# 如：斐波那契数列
dp[i] = dp[i-1] + dp[i-2]
```

#### 2. **多状态线性DP**
```python
# 如：买卖股票
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])  # 不持有
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])  # 持有
```

#### 3. **带约束的线性DP**
```python
# 如：打家劫舍（不能相邻）
dp[i] = max(dp[i-1], dp[i-2] + nums[i])
```

---

## 3. 状态压缩与线性DP的关系

### 1. **线性DP是状态压缩的基础**
- 线性DP通常用一维数组，天然适合状态压缩
- 状态压缩是线性DP的优化手段

### 2. **状态压缩的应用场景**
- 当线性DP的空间复杂度可以进一步优化时
- 当只需要前几个状态时，可以用滚动数组
- 当状态可以用位运算表示时

### 3. **实际应用示例**
```python
# 线性DP + 状态压缩
def optimized_fib(n):
    if n <= 1:
        return n
    
    # 状态压缩：只保存前两个值
    prev2, prev1 = 0, 1
    
    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    
    return prev1
```

---

## 4. 总结

### 状态压缩的核心思想：
1. **减少空间复杂度**：从O(n²)降到O(n)
2. **保持正确性**：确保状态转移逻辑不变
3. **注意遍历顺序**：避免状态被错误覆盖
4. **合理使用技巧**：滚动数组、位运算等

### 线性DP的核心思想：
1. **状态简单**：通常用一维数组
2. **转移直观**：只依赖前几个状态
3. **实现容易**：代码结构清晰
4. **应用广泛**：很多问题都可以转化为线性DP

### 学习建议：
1. 先掌握线性DP的基本模式
2. 理解状态压缩的优化原理
3. 通过大量练习熟悉各种变种
4. 注意边界条件和遍历顺序

状态压缩和线性DP是动态规划中的重要概念，掌握它们对于解决复杂的DP问题非常有帮助！

























































