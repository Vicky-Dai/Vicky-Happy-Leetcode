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


"""
DP
Bottom UP
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True # 递归转化成dp，termination condition
        # if i == len(s): return True 变成初始化条件

        for i in range(len(s)-1, -1, -1): # 递归回来收集，所以逆向
            for word in wordDict:
                if i + len(word) <= len(s):
                    if s[i:i+len(word)] == word:
                        dp[i] = dp[i+len(word)]
                    if dp[i]:  # 这个一定要注意，相当于遇到直接返回，不然结果可能被后面不可行的改变
                        break
        return dp[0]

""" 
Recursion
 t*m^n   n
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def dfs(i):
            if i == len(s):
                return True

            for w in wordDict:
                if ((i + len(w)) <= len(s) and
                     s[i : i + len(w)] == w
                ):
                    if dfs(i + len(w)):
                        return True
            return False

        return dfs(0)