# 动态规划基础模板总结

## 动态规划五部曲
1. **确定dp数组以及下标的含义**
2. **确定递推公式**
3. **dp数组如何初始化**
4. **确定遍历顺序**
5. **举例推导dp数组**

---

## 1. 线性DP模板

### 1.1 斐波那契数列类型
```python
class Solution:
    def fib(self, n: int) -> int:
        # 1. dp[i] 表示第i个斐波那契数
        # 2. 递推公式: dp[i] = dp[i-1] + dp[i-2]
        # 3. 初始化: dp[0] = 0, dp[1] = 1
        # 4. 遍历顺序: 从前往后
        # 5. 举例推导
        
        if n <= 1:
            return n
        
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

# 状态压缩版本
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        prev2, prev1 = 0, 1
        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        
        return prev1
```

### 1.2 爬楼梯类型
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        # 1. dp[i] 表示爬到第i阶的方法数
        # 2. 递推公式: dp[i] = dp[i-1] + dp[i-2]
        # 3. 初始化: dp[1] = 1, dp[2] = 2
        # 4. 遍历顺序: 从前往后
        
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
```

### 1.3 最小花费爬楼梯
```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 1. dp[i] 表示到达第i阶的最小花费
        # 2. 递推公式: dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        # 3. 初始化: dp[0] = cost[0], dp[1] = cost[1]
        # 4. 遍历顺序: 从前往后
        
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        
        return min(dp[n-1], dp[n-2])
```

---

## 2. 背包DP模板

### 2.1 01背包（一维数组）
```python
class Solution:
    def knapsack01(self, weights: List[int], values: List[int], capacity: int) -> int:
        # 1. dp[j] 表示容量为j的背包能装的最大价值
        # 2. 递推公式: dp[j] = max(dp[j], dp[j-weight[i]] + value[i])
        # 3. 初始化: dp[0] = 0
        # 4. 遍历顺序: 先物品后背包，背包从后往前遍历
        
        n = len(weights)
        dp = [0] * (capacity + 1)
        
        for i in range(n):  # 先遍历物品
            for j in range(capacity, weights[i] - 1, -1):  # 后遍历背包，从后往前
                dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
        
        return dp[capacity]
```

### 2.2 完全背包（一维数组）
```python
class Solution:
    def knapsackComplete(self, weights: List[int], values: List[int], capacity: int) -> int:
        # 1. dp[j] 表示容量为j的背包能装的最大价值
        # 2. 递推公式: dp[j] = max(dp[j], dp[j-weight[i]] + value[i])
        # 3. 初始化: dp[0] = 0
        # 4. 遍历顺序: 先物品后背包，背包从前往后遍历
        
        n = len(weights)
        dp = [0] * (capacity + 1)
        
        for i in range(n):  # 先遍历物品
            for j in range(weights[i], capacity + 1):  # 后遍历背包，从前往后
                dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
        
        return dp[capacity]
```

### 2.3 多重背包
```python
class Solution:
    def knapsackMultiple(self, weights: List[int], values: List[int], nums: List[int], capacity: int) -> int:
        # 1. dp[j] 表示容量为j的背包能装的最大价值
        # 2. 递推公式: dp[j] = max(dp[j], dp[j-k*weight[i]] + k*value[i])
        # 3. 初始化: dp[0] = 0
        # 4. 遍历顺序: 先物品后背包，背包从后往前遍历
        
        n = len(weights)
        dp = [0] * (capacity + 1)
        
        for i in range(n):  # 先遍历物品
            for j in range(capacity, weights[i] - 1, -1):  # 后遍历背包，从后往前
                for k in range(1, nums[i] + 1):  # 遍历物品数量
                    if j >= k * weights[i]:
                        dp[j] = max(dp[j], dp[j - k * weights[i]] + k * values[i])
        
        return dp[capacity]
```

---

## 3. 子序列DP模板

### 3.1 最长递增子序列（LIS）
```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 1. dp[i] 表示以nums[i]结尾的最长递增子序列长度
        # 2. 递推公式: dp[i] = max(dp[i], dp[j] + 1) if nums[i] > nums[j]
        # 3. 初始化: dp[i] = 1
        # 4. 遍历顺序: 外层遍历i，内层遍历j(0到i-1)
        
        n = len(nums)
        dp = [1] * n
        result = 1
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i])
        
        return result
```

### 3.2 最长公共子序列（LCS）
```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 1. dp[i][j] 表示text1[0:i]和text2[0:j]的最长公共子序列长度
        # 2. 递推公式: 
        #    if text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
        #    else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # 3. 初始化: dp[0][j] = 0, dp[i][0] = 0
        # 4. 遍历顺序: 从前往后
        
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]
```

### 3.3 编辑距离
```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 1. dp[i][j] 表示word1[0:i]转换为word2[0:j]的最小操作数
        # 2. 递推公式:
        #    if word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1]
        #    else: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        # 3. 初始化: dp[0][j] = j, dp[i][0] = i
        # 4. 遍历顺序: 从前往后
        
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 初始化
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
        return dp[m][n]
```

### 3.4 最大子数组和
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 1. dp[i] 表示以nums[i]结尾的最大子数组和
        # 2. 递推公式: dp[i] = max(nums[i], dp[i-1] + nums[i])
        # 3. 初始化: dp[0] = nums[0]
        # 4. 遍历顺序: 从前往后
        
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        result = dp[0]
        
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            result = max(result, dp[i])
        
        return result

# 状态压缩版本
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = nums[0]
        result = prev
        
        for i in range(1, len(nums)):
            curr = max(nums[i], prev + nums[i])
            result = max(result, curr)
            prev = curr
        
        return result
```

---

## 4. 矩阵DP模板

### 4.1 不同路径
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1. dp[i][j] 表示从(0,0)到(i,j)的路径数
        # 2. 递推公式: dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # 3. 初始化: dp[0][j] = 1, dp[i][0] = 1
        # 4. 遍历顺序: 从前往后
        
        dp = [[0] * n for _ in range(m)]
        
        # 初始化第一行和第一列
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
```

### 4.2 最大正方形
```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 1. dp[i][j] 表示以(i,j)为右下角的最大正方形边长
        # 2. 递推公式: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        # 3. 初始化: dp[0][j] = 1 if matrix[0][j] == '1', dp[i][0] = 1 if matrix[i][0] == '1'
        # 4. 遍历顺序: 从前往后
        
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        maxSide = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        
        return maxSide * maxSide
```

### 4.3 最小路径和
```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 1. dp[i][j] 表示从(0,0)到(i,j)的最小路径和
        # 2. 递推公式: dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        # 3. 初始化: dp[0][0] = grid[0][0]
        # 4. 遍历顺序: 从前往后
        
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        
        dp[0][0] = grid[0][0]
        
        # 初始化第一行
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # 初始化第一列
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[m-1][n-1]
```

---

## 5. 特殊DP模板

### 5.1 打家劫舍
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1. dp[i] 表示偷到第i个房屋时的最大金额
        # 2. 递推公式: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        # 3. 初始化: dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
        # 4. 遍历顺序: 从前往后
        
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[n-1]
```

### 5.2 买卖股票（状态机DP）
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1. dp[i][0] 表示第i天持有股票的最大利润
        #    dp[i][1] 表示第i天不持有股票的最大利润
        # 2. 递推公式:
        #    dp[i][0] = max(dp[i-1][0], -prices[i])
        #    dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        # 3. 初始化: dp[0][0] = -prices[0], dp[0][1] = 0
        # 4. 遍历顺序: 从前往后
        
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        
        dp[0][0] = -prices[0]  # 持有股票
        dp[0][1] = 0           # 不持有股票
        
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        
        return dp[n-1][1]
```

---

## 总结

### 关键要点：
1. **线性DP**：通常是一维数组，状态转移相对简单
2. **背包DP**：注意遍历顺序，01背包从后往前，完全背包从前往后
3. **子序列DP**：通常需要两层循环，外层遍历当前位置，内层遍历之前的位置
4. **矩阵DP**：二维数组，注意边界条件的初始化
5. **状态机DP**：用多个状态表示不同的情况，如买卖股票

### 通用解题步骤：
1. 分析问题，确定状态定义
2. 找出状态转移方程
3. 确定初始状态
4. 确定遍历顺序
5. 考虑空间优化（状态压缩）
