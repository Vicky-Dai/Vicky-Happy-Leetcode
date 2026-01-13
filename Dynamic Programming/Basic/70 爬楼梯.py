class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1: # first think of special cases
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1 # walk one step, there is only 1 way
        dp[2] = 2 # walk two steps, there are 2 ways
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]