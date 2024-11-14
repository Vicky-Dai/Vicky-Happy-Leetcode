class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words: return []
        result = []
        hash = [0] * 26 # 用来统计所有字符串里字符出现的最小频率
        for i, c in enumerate(words[0]):  # 用第一个字符串给hash初始化 #enumerate(words[0]) 是一个 Python 内置函数，用于将一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列，同时列出数据和数据下标。
            hash[ord(c) - ord('a')] += 1
        # 统计除第一个字符串外字符的出现频率
        for i in range(1, len(words)):
            hashOtherStr = [0] * 26
            for j in range(len(words[i])):
                hashOtherStr[ord(words[i][j]) - ord('a')] += 1
            # 更新hash，保证hash里统计26个字符在所有字符串里出现的最小次数
            for k in range(26):
                hash[k] = min(hash[k], hashOtherStr[k])
        # 将hash统计的字符次数，转成输出形式
        for i in range(26):
            while hash[i] != 0: # 注意这里是while，多个重复的字符
                result.extend(chr(i + ord('a')))
                hash[i] -= 1
        return result