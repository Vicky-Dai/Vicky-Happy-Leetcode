#栈头到栈底，递增单调栈
#遍历数组，情况1和情况2：当前元素小于 等于栈顶元素，把当前元素入栈 
# 情况3：栈顶元素大于栈顶元素，栈顶元素出栈，在栈顶元素（数组下标）所在位置计算出和当前元素的距离，存入结果

class Solution:
    def dailyTemperatures(self, T: list[int]) -> list[int]:
        result = [0] * len(T)
        stack = [0] #栈用来存放遍历过的元素，第一个就是，所以初始化为0 后面要保证递增
        for i in range(1, len(T)):
            #情况1和情况2
            if T[i] <= T[-1]:
                stack.append(i)
            #情况3
            else:
                while len(stack) != 0 and T[i] > T[stack[-1]]:
                    result[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        return result
        