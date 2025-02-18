class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_occurrence = {} #存储每个字母的最远下标位置，其实很简单，遍历一遍，每次都更新就好了，因为下表是递增的
        for i, ch in enumerate(s):
            last_occurrence[ch] = i

        result = []
        start = 0
        end = 0 #用于找到当前字符出现的最远位置
        for i, ch in enumerate(s):
            end = max(end, last_occurrence[ch]) #end 表示当前分区的最远右边界，它随着 i 的遍历不断更新，确保区间内的所有字符都能被完全包含。max(end, last_occurrence[ch]) 保证了当前分区能容纳所有出现的字符，不会把属于同一分区的字符拆开。
            if end == i:
                result.append(end - start + 1)
                start = i + 1

        return result

