# 滑动窗口
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isVowel(ch):
            return int(ch in "aeiou")
        
        n = len(s)
        vowel_count = sum(1 for i in range(k) if isVowel(s[i]))
        ans = vowel_count
        for i in range(k, n):
            vowel_count += isVowel(s[i]) - isVowel(s[i - k])
            ans = max(ans, vowel_count)
        return ans

""" s[i] 是当前窗口进入的新字符。

s[i - k] 是当前窗口退出的旧字符。 """