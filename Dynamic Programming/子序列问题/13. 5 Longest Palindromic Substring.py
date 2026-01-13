# DP Time: O(n^2) Space: O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)] # dp[i][j] 表示 s[i:j+1] 是否为回文串
        
        start, max_len = 0, 1
        
        for i in range(n):
            dp[i][i] = True
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1] #因为i+1 j-1 已经判断过了，所以这里可以直接用
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    start = i
        
        return s[start:start + max_len]


# 中心扩散 Two Pointers Time: O(n^2) Space: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # 以 s[i] 为中心的最长回文子串
            s1 = self.palindrome(s, i, i)
            # 以 s[i] 和 s[i+1] 为中心的最长回文子串
            s2 = self.palindrome(s, i, i + 1)
            # res = longest(res, s1, s2)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res

    def palindrome(self, s: str, l: int, r: int) -> str:
        # 防止索引越界
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # 向两边展开
            l -= 1
            r += 1
        # 此时 s[l+1..r-1] 就是最长回文串
        return s[l + 1:r]