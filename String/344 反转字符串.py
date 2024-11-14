class Solution:
    def reversestr(self, string:list[str] )->list[str]: #string:list[str]字符串列表可以改变，字符串无法改变
        s = len(string)
        left = 0
        right = s-1
        for i in range(s//2):
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1

        return string

solution = Solution()
    
#test1
string = ["1", "3", "4", "2", "5"]
result = solution.reversestr(string)
result_str = ''.join(result) #.join() 是 Python 字符串方法之一，用于将一个可迭代对象（如列表、元组等）中的元素连接成一个单一的字符串。
print(result_str)


    