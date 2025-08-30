# 懒惰双指针+哈希表
# 懒惰双指针的原因是左指针并没有真正的挪动，实际上很多时候懒惰很有用

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
