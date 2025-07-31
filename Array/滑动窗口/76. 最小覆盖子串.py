class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        record, tmap = defaultdict(int), defaultdict(int)
        
        for le in t:
            tmap[le] += 1

        left, right = 0, 0
        start = 0  # 最小窗口起点
        valid = 0  # 当前已经满足条件的字符数
        length = float('inf')

        while right < len(s):
            c = s[right]
            right += 1
            if c in tmap:
                record[c] += 1
                if record[c] == tmap[c]:  # ⚠️ 注意：这里要写在 record[c] += 1 之后
                    valid += 1

            while valid == len(tmap):
                # 更新最小子串
                if right - left < length:
                    length = right - left
                    start = left

                d = s[left]
                left += 1
                if d in tmap:
                    if record[d] == tmap[d]:  # ⚠️ 注意先检查再减
                        valid -= 1
                    record[d] -= 1

        return "" if length == float('inf') else s[start: start + length]
