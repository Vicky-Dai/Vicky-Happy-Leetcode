class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26 #使用数组作为哈希表
        for i in s: #遍历的是字符串 s 中的每个字符。在 Python 中，字符串可以被视为一个字符序列，因此可以使用 for 循环来遍历其中的每个字符。
            #并不需要记住字符a的ASCII，只要求出一个相对数值就可以了
            record[ord(i) - ord("a")] += 1 #ord(i)：获取字符 i 的 ASCII 码值。
        for i in t:
            record[ord(i) - ord("a")] -= 1
        for i in range(26):
            if record[i] != 0:
                #record数组如果有的元素不为零0，说明字符串s和t 一定是谁多了字符或者谁少了字符。
                return False
        return True