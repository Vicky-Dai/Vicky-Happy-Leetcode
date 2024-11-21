#其实这道题跟1143是一模一样的，相同子序列保证顺序相同，保证不会相交

class Solution:
    def maxUncrossedLines(self, A:list[int], B:list[int]) -> int:
        dp = [[0]*len(B) for _ in range(len(A))]
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len(A)][len(B)]