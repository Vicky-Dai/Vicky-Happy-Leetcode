# 左右指针窗口

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        left, right = 0, 0
        maxLen = 0
        for right, char in enumerate(s):
            if char in char_dict and char_dict[char] >= left: # 注意这里要保证char_dict[char] >= left，否则有可能会回退
                left = char_dict[char] + 1
            char_dict[char] = right 
            maxLen = max(maxLen, right-left+1)
        return maxLen
