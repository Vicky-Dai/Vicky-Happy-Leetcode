# 子问题：字符串 s 的前 i 个字符能否被字典 wordDict 拆分？
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict) 
        n = len(s)
        dp = [False] *(n+1) # dp[i] = s[:i]（前 i 个字符）能否被 wordDict 拆分出来
        dp[0] = True # 空字符串可以被拆分成单词
        for j in range(1, n+1):
            for i in range(j):
                if dp[i] and s[i:j] in wordSet:
                    dp[j] = True
                    break
        return dp[-1]
""" 如果前一段能完成拆分
并且后一段是一个字典词
那么整个前 j 个字符都能拆分 """