#

""" 
思路：
移除多余空格
将整个字符串反转
将每个单词反转
 """

class Solution:
    def single_reverse(self, s, start: int, end: int):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def reverseWords(self, s: str) -> str:
        result = ""
        fast = 0
        # 1. 首先将原字符串反转并且除掉空格, 并且加入到新的字符串当中
        # 由于Python字符串的不可变性，因此只能转换为列表进行处理
        s = list(s)
        s.reverse()
        while fast < len(s):
            if s[fast] != " ":
                if len(result) != 0: # 如果不是第一个单词，那么就加一个空格
                    result += " "
                while s[fast] != " " and fast < len(s): # 一次性把一个单词给加进去
                    result += s[fast]
                    fast += 1
            else: # 如果是空格，那么就跳过
                fast += 1
        # 2.其次将每个单词进行翻转操作
        slow = 0
        fast = 0
        result = list(result)
        while fast <= len(result):
            if fast == len(result) or result[fast] == " ":
                self.single_reverse(result, slow, fast - 1) # 单个翻转交给一个函数来处理
                slow = fast + 1 # 每次翻转完毕之后，slow和fast都要往前走
                fast += 1
            else:
                fast += 1 # 如果不是空格，那么就继续往前走

        return "".join(result)

class Solution:
    def reverseWords(self, s: str) -> str:
        #反转字符串
        s = s[::-1]
        # 把字符串拆分为单词，并且翻转每个单词
        # split() 函数能够自动忽略多余的空白字符
        s = ' '.join(word[::-1] for word in s.split())
        return s





# split 基本语法 str.split(separator=None, maxsplit=-1)
# separator用于分割字符串的分隔符  maxsplit指定最大分割次数， 默认-1 次数不限制
