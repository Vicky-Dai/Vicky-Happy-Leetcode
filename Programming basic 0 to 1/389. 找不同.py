# 枚举
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnt = [0] * 26  # 26个小写字母的频次数组
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
        for ch in t:
            cnt[ord(ch) - ord('a')] -= 1
            if cnt[ord(ch) - ord('a')] < 0:
                return ch
