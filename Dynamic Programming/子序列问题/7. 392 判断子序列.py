#不连续 相对位置不变 子序列    同求最长公共子序列1143
#dp[i][j] i-1为结尾的字符串s和j-1为结尾的字符串t的相同子序列的长度
#dp[i][0] = 0  dp[0][j] = 0

class Solution:
    def isSubsequence(self, s:str, t:str) -> bool:
        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)] #这里注意+1   行是s 列是t，只有t可以缩短（或理解为切割）
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1 
                else:
                    dp[i][j] = dp[i][j-1] #从左侧推出 因为只有j可以缩短 s不能变
        if dp[-1][-1] == len(s):
            return True
        return False