#dp[i][j]：字符串s在[i, j]范围内最长的回文子序列的长度为dp[i][j]。
#如果s[i]与s[j]相同，那么dp[i][j] = dp[i + 1][j - 1] + 2;
# 如果s[i]与s[j]不相同，说明s[i]和s[j]的同时加入 并不能增加[i,j]区间回文子序列的长度，那么分别加入s[i]、s[j]看看哪一个可以组成最长的回文子序列。

# 加入s[j]的回文子序列长度为dp[i + 1][j]。

# 加入s[i]的回文子序列长度为dp[i][j - 1]。

# 那么dp[i][j]一定是取最大的，即：dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);

# 这道题初始化比较有意思，最初的状态其实是从中间来的，也就是i和j相同的时候

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2 #如果s[i]与s[j]相同，那么dp[i][j] = dp[i + 1][j - 1] + 2; 把这两个相等的加上
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1]) #看看考虑最左边和最右边哪一个可以组成最长的回文子序列
        return dp[0][-1]