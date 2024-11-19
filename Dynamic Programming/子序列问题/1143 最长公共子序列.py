#元素要保持顺序，但可以不连续
#dp[i][j] ：以下标i - 1为结尾的A，和以下标j - 1为结尾的B，最长重复子数组长度为dp[i][j]。 （特别注意： “以下标i - 1为结尾的A” 标明一定是 以A[i-1]为结尾的字符串 ）
#这道题的递推很有意思啊，会有if else， 不是仅仅从[i-1][j-1]推出来了，这是因为，这道题不要求连续，所以nums12不是共进退的
#和718连续二维的区别：把二维数组画出来，就会发现718连续，都是从对角线左上角推过来的（因为共进退）；而和之前一个数组不连续的区别，就是这个是二维的，所以有多个方向。我觉得 不要和300对比 容易混淆

class Solution:
    def longestCommonSubsequence(self, text1:str, text2:str) -> int:
        dp = [[0]*len(text2) for _ in range(len(text1))]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else: 
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) ## 如果 text1[i-1] 和 text2[j-1] 不相等，则当前位置的最长公共子序列长度为上方或左方的较大值
        return dp[len(text1)][len(text2)]