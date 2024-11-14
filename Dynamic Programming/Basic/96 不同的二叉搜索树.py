#分析子状态之间的关系很重要
#具体案例分析 dp[3] = dp[0]*dp[2] + dp[1]*dp[1] + dp[2]*dp[0]

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)  #dp[i] 含义，有i个节点时候，有几种组合方式
        dp[0] = 1 #dp[1] 可以推导出来
        for i in range(1, n+1): #i是过去每个子问题的n
            for j in range(1, i+1): #j是每个字问题分情况讨论，j作为头结点，分左右子树
                dp[i] += dp[j-1]*dp[i-j]
        return dp[n]
