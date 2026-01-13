#dp[i][j] i-1为结尾的word1和以j-1为结尾的word2的最小编辑距离

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            dp[i][0] = i #初始化，要删除i个字符
        for j in range(len(word2)+1):
            dp[0][j] = j
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] #如果当前字符相等，那么不需要操作，就来自于上一步左上方的值
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 #1. 替换元素 2.删除word1一个元素，那么就是以下标i - 2为结尾的word1 与 j-1为结尾的word2的最近编辑距离 再加上一个操作
                    #3.删除word2一个元素，那么就是以下标i - 1为结尾的word1 与 j-2为结尾的word2的最近编辑距离 再加上一个操作
        return dp[-1][-1]

INDEX 记录下来  查找删除插入 O(1)
设计  二分法

递归 memory search  dp rolling arry

0 length-1
