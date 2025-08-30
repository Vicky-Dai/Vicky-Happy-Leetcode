#（版本一）先删除空白，然后整个反转，最后单词反转。 因为字符串是不可变类型，所以反转单词的时候，需要将其转换成列表，然后通过join函数再将其转换成列表，所以空间复杂度不是O(1)

class Solution:
    def reverseWords(self, s: str) -> str:
        # 反转整个字符串
        s = s[::-1]
        # 将字符串拆分为单词，并反转每个单词
        # split()函数能够自动忽略多余的空白字符
        s = ' '.join(word[::-1] for word in s.split())
        return s
    
#（版本二）使用双指针

class Solution:
    def reverseWords(self, s: str) -> str:
        # 将字符串拆分为单词，即转换成列表类型
        words = s.split()

        # 反转单词
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        # 将列表转换成字符串
        return " ".join(words)
    
# (版本三) 拆分字符串 + 反转列表

class Solution:
    def reverseWords(self, s):
        words = s.split() #type(words) --- list
        words = words[::-1] # 反转单词
        return ' '.join(words) #列表转换成字符串
    
# (版本四) 将字符串转换为列表后，使用双指针去除空格

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
                if len(result) != 0:
                    result += " "
                while s[fast] != " " and fast < len(s):
                    result += s[fast]
                    fast += 1
            else:
                fast += 1
        # 2.其次将每个单词进行翻转操作
        slow = 0
        fast = 0
        result = list(result)
        while fast <= len(result):
            if fast == len(result) or result[fast] == " ":
                self.single_reverse(result, slow, fast - 1)
                slow = fast + 1
                fast += 1
            else:
                fast += 1

        return "".join(result)
    
# (版本五) 遇到空格就说明前面的是一个单词，把它加入到一个数组中。

class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ''
        s += ' ' # 帮助处理最后一个字词

        for char in s:
            if char == ' ': # 遇到空格就说明前面的可能是一个单词
                if word != '': # 确认是单词，把它加入到一个数组中
                    words.append(word)
                    word = '' # 清空当前单词
                continue
            
            word += char # 收集单词的字母
        
        words.reverse()
        return ' '.join(words)
    
# 原地修改版本
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
