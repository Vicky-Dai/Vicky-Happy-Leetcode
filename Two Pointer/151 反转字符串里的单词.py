#

""" 
思路：
移除多余空格
将整个字符串反转
将每个单词反转
 """

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
