# 未优化版滑动窗口
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        ori = Counter(t)  # t 中每个字符的目标次数
        cnt = defaultdict(int)  # 当前窗口中每个字符出现的次数

        def check():
            for c in ori:
                if cnt[c] < ori[c]:
                    return False
            return True

        l = 0
        r = -1
        min_len = float('inf')
        ans_l = 0

        while r < len(s) - 1:
            r += 1
            if s[r] in ori:
                cnt[s[r]] += 1

            while check() and l <= r:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    ans_l = l
                if s[l] in ori:
                    cnt[s[l]] -= 1
                l += 1

        return "" if min_len == float('inf') else s[ans_l:ans_l + min_len]


# 优化 只关心 t 中的字符、预先跳过无关字符的预处理思路。
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        ori = Counter(t)
        required = len(ori)

        # 过滤 s，只保留 t 中出现的字符及其原始索引
        filtered_s = [(i, c) for i, c in enumerate(s) if c in ori]

        l = r = 0
        formed = 0
        window_counts = {}
        ans = float('inf'), None, None  # (长度, 左边界, 右边界)

        while r < len(filtered_s):
            idx_r, char_r = filtered_s[r]
            window_counts[char_r] = window_counts.get(char_r, 0) + 1

            if window_counts[char_r] == ori[char_r]:
                formed += 1 #formed 来表示：当前窗口中有多少种字符达到了 t 中要求的频率。

            while l <= r and formed == required: # 找到了
                idx_l, char_l = filtered_s[l]
                window_len = idx_r - idx_l + 1
                if window_len < ans[0]:
                    ans = (window_len, idx_l, idx_r)

                window_counts[char_l] -= 1
                if window_counts[char_l] < ori[char_l]:
                    formed -= 1
                l += 1

            r += 1

        return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]
