# Method 1:
# Recursion (not efficent) time complexity: O(2^n) space complexity: O(n)
class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        return self.fib(n-1) + self.fib(n-2)

# Method 2:
# Recursion with Memoization time complexity: O(n) space complexity: O(n)
def fib(n: int) -> int:
    # 备忘录全初始化为 -1
    # 因为斐波那契数肯定是非负整数，所以初始化为特殊值 -1 表示未计算

    # 因为数组的索引从 0 开始，所以需要 n + 1 个空间
    # 这样才能把 `f(0) ~ f(n)` 都记录到 memo 中
    memo = [-1] * (n + 1)

    return self.dp(memo, n)

# 带着备忘录进行递归
def dp(memo: list, n: int) -> int:
    # base case
    if n == 0 or n == 1:
        return n
    # 已经计算过，不用再计算了
    if memo[n] != -1:
        return memo[n]
    # 在返回结果之前，存入备忘录
    memo[n] = self.dp(memo, n - 1) + self.dp(memo, n - 2)
    return memo[n]

# Method 3:
# DP Table time complexity: O(n) space complexity: O(n)
class Solution:
    def fib(self, n: int) -> int:
       
        # 排除 Corner Case
        if n == 0:
            return 0
        
        # 创建 dp table 
        dp = [0] * (n + 1)

        # 初始化 dp 数组
        dp[0] = 0
        dp[1] = 1 

        # 遍历顺序: 由前向后。因为后面要用到前面的状态
        for i in range(2, n + 1):

            # 确定递归公式/状态转移公式
            dp[i] = dp[i - 1] + dp[i - 2]
        
        # 返回答案
        return dp[n]
    
# Method 4:
# State Compression time complexity: O(n) space complexity: O(1)
#在状态转移的过程中，其实你会发现，其实只要维护三个值就可以了，所以就可以压缩空间
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        dp = [0, 1]
        
        for i in range(2, n + 1):
            total = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = total
        
        return dp[1]
    

#还可以用双指针