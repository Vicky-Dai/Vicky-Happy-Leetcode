class Solution:
    def reverseWords(self, s:str) -> str:
        s = s.strip() #删除前后空白
        s = s[::-1] #[]切片操作 [start:end:step] 如果没写就是从头到尾， step为负表示从后往前  所以这是一个反转字符串操作
        #字符串拆分为单词，并反转每个单词
        s = ' '.join((word[::-1]) for word in s.split()) #注意引号中间要保留空格
        #split() 方法接受一个模式，通过搜索模式将字符串分割成一个有序的子串列表，将这些子串放入一个数组，并返回该数组。 字符串不可变 所以要换成列表
        #这一句是生成器表达式 result = 函数[表达式for 变量in可迭代对象]表达式 是对 变量 的处理，比如你提到的 word[::-1] 这种反转操作。
        #最终，整个生成器表达式被作为参数传递给一个函数，比如 join，或者直接生成一个列表、集合、字典等。
        #join回吧元素用前面的字符串（这里是空格）相链接
        return s 
    
#test
solution = Solution()
s ="   love the way you lie "
result = solution.reverseWords(s)
print(result)