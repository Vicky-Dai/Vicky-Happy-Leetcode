# 方法 1: 数组在哈西法的应用
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = [0] * 2001
        for i in range(len(arr)):
            count[arr[i] + 1000] += 1 # 防止负数作为下标
        freq = [False] * 1001 # 标记相同频率是否重复出现
        for i in range(2001):
            if count[i] > 0:
                if freq[count[i]] == False:
                    freq[count[i]] = True
                else:
                    return False
        return True