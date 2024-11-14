class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_occurrence = {} #存储每个字母的最远下标位置，其实很简单，遍历一遍，每次都更新就好了，因为下表是递增的
        for i, ch in enumerate(s):
            last_occurrence[ch] = i

        result = []
        start = 0
        end = 0 #用于找到当前字符出现的最远位置
        for i, ch in enumerate(s):
            end = max(end, last_occurrence[ch])
            if end == i:
                result.append(end - start + 1)
                start = i + 1

        return result

