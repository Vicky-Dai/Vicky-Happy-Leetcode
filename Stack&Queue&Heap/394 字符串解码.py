class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[': # 遇到左括号，先把当前的结果和数字压入栈中 并且重置
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']': # 遇到右括号，先把当前的结果和数字弹出栈中，计算当前的结果
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)   # 处理数字拼接         
            else:
                res += c
        return res
