#时间复杂度: O(n)
#空间复杂度: O(n)
# 第一种情况：已经遍历完了字符串，但是栈不为空，说明有相应的左括号没有右括号来匹配，所以return false

# 第二种情况：遍历字符串匹配的过程中，发现栈里没有要匹配的字符。所以return false

# 第三种情况：遍历字符串匹配的过程中，栈已经为空了，没有匹配的字符了，说明右括号没有找到对应的左括号return false
# 但还有一些技巧，在匹配左括号的时候，右括号先入栈，就只需要比较当前元素和栈顶相不相等就可以了，比左括号先入栈代码实现要简单的多了！

#第一种方法 只用栈 仅使用栈，更省空间
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(')')
            elif item == '{':
                stack.append('}')
            elif not stack or stack[-1] != item:
                return False #第三种情况（缺左）和第二种情况情况  注意要把not stack写在前面 不然如果对空栈操作会报错
            else:
                stack.pop() #正常情况对弹出元素

        return True if not stack else False #或 return not stack
    # 三元表达式 如果 stack 为空（即 not stack 为 True），则返回 True；否则返回 False。 这里考虑了第一种情况，遍历完了看是栈不为空说明左边多了一个


#方法二 字典
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for item in s:
            if item in mapping.keys():
                stack.append(mapping[item])
            elif not stack or stack[-1]:
                return False
            else:
                stack.pop()
        return True if not stack else False
    
#简化版  思路很清晰 推荐！！ 先分左右 然后判断的三种情况 其中两个扔在右边，最后一个扔在最后
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # 通过字典映射来简化代码
        pairs = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in pairs:  # 当前字符是右括号 检查的是键
                if not stack or stack[-1] != pairs[char]:  # 栈为空或栈顶不匹配
                    return False
                stack.pop()  # 匹配成功，弹出栈顶元素
            else:
                stack.append(char)  # 当前字符是左括号，压入栈
                
        return not stack  # 如果栈为空，表示所有括号匹配成功
