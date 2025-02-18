#时间复杂度: O(n)
#空间复杂度: O(n)

from operator import add, sub, mul

def div(x, y):
    # 使用整数除法的向零取整方式
    return int(x / y) if x * y > 0 else -(abs(x) // abs(y))
#当两个数相乘的结果为负时，手动取绝对值后做整除，再添加负号，以实现向零取整。INF
class Solution(object):
    op_map = {'+': add, '-': sub, '*': mul, '/': div} #op_map 字典将操作符映射到对应的操作函数
    #原先+-*只是字符串，因为题目是an array of strings  需要把它们映射成运算，但是运算符不能直接作为函数使用 不能直接传递或者赋值给变量
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}: #如果当前 token 不是运算符，直接将其转换为整数并压入栈中。
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop() #注意顺序 op1 是第一个弹出的操作数，它应该在运算符的左边。
                stack.append(self.op_map[token](op1, op2))  # 第一个出来的在运算符后面  右开口的栈
        return stack.pop()
    

""" 如何计算逆波兰表达式？
计算逆波兰表达式通常使用堆栈（stack）来实现：

从左到右扫描表达式。
遇到操作数时，将其推入堆栈。
遇到运算符时，从堆栈中弹出相应的操作数，进行计算，再将结果推回堆栈。
最终，堆栈中只剩下一个元素，这个元素就是表达式的结果。 """