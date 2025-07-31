class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        left, right, valid = 0, 0, 0
        smap, window = defaultdict(int), defaultdict(int)
        for c in s1:
            smap[c] += 1
        while right < len(s2):
            s = s2[right]
            right += 1
            if s in smap:
                window[s] += 1
                if window[s] == smap[s]:
                    valid += 1

            while right - left >= len(s1): #!!!!!!!!!!!
                if valid == len(smap):
                    return True
                d = s2[left]
                left += 1
                if d in smap: #!!!!!!!!!
                    if window[d] == smap[d]:  # only when they equal
                        valid -= 1
                    window[d] -= 1
        return False
