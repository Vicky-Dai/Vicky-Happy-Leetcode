# 基于编辑距离的写法
#dp[i][j]：以i-1为结尾的字符串word1，和以j-1位结尾的字符串word2，想要达到相等，所需要删除元素的最少次数。、class Solution:
#dp[i][j] = 让 word1 的前 i 个字符 和 word2 的前 j 个字符 完全相等所需的最少删除次数。
#
class Solution:    
    def minDistance(self, word1: str, word2: str) -> int:
            dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
            for i in range(len(word1)+1): # “word2 是空串，要把 word1[:i] 变成空串，只能删掉它的 i 个字符。”
                dp[i][0] = i 
            for j in range(len(word2)+1):
                dp[0][j] = j
            for i in range(1, len(word1)+1):
                for j in range(1, len(word2)+1):
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(dp[i-1][j-1] + 2, dp[i-1][j] + 1, dp[i][j-1] + 1)
            # 加2是因为让 word1[i-1] 和 word2[j-1] 都消失
            return dp[-1][-1]



# 基于LCS的写法
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # dp[i][j]：word1 前 i 个字符 和 word2 前 j 个字符 的最长公共子序列长度（LCS）
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                # 如果两个字符串的当前尾字符相同
                # LCS 可以加 1：保留这两个字符
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

                else:
                    # 如果当前字符不同，则这两个字符无法同时出现在 LCS 中
                    # LCS = 去掉 word1 尾巴 或 去掉 word2 尾巴，两者中较大的
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # 最长公共子序列长度
        lcs = dp[m][n]

        # 两个字符串都需要删除非 LCS 的字符
        # word1 删掉 m - lcs 个
        # word2 删掉 n - lcs 个
        return m + n - 2 * lcs
