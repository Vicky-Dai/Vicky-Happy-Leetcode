#时间复杂度: O(n)
#空间复杂度: O(n)，返回值不计空间复杂度

#方法一：栈
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list()
        for item in s:
            if res and res[-1] == item: #里面有元素且item和上一个相等
                res.pop()
            else:
                res.append(item)

        return "".join(res) #把栈里面剩下的元素拼接成字符串 只是为了把列表变成字符串而已
    

# 方法二，使用双指针模拟栈，如果不让用栈可以作为备选方法。
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list(s)
        slow = fast = 0
        length = len(res)

        while fast < length:
            # 如果一样直接换，不一样会把后面的填在slow的位置
            res[slow] = res[fast]
            
            # 如果发现和前一个一样，就退一格指针
            if slow > 0 and res[slow] == res[slow - 1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
            
        return ''.join(res[0: slow])