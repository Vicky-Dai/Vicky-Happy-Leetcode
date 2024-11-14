#要找单调递增的最大值，模拟一下，发现从前往后不可行，要从后往前
#这道题有细节要注意：1.flag的定义和修改

class Solution:
    def monotoneIncreasingDigits(self, N:int) -> int:
        #将整数转换为字符串
        strNum = str(N)
        #flag定义 用来标记赋值9从哪里开始
        flag = len(strNum)

        for i in range(len(strNum) - 1, 0, -1):
            if strNum[i-1] > strNum[i]:
                flag = i
                # strNum[i-1] = str(int(strNum[i-1])-1) #字符串没法直接减一  # 'str' object does not support item assignment
                strNum = strNum[:i - 1] + str(int(strNum[i - 1]) - 1) + strNum[i:]

        #将flag位置以及之后的字符都修改为9，保证最大的递增数字
        for i in range(flag, len(strNum)):
            strNum = strNum[:i] + '9' + strNum[i + 1:]

        #将最终的字符串转换回整数返回
        return int(strNum) 


#简化版
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        strNum = str(N)        
        for i in range(len(strNum) - 1, 0, -1):
            # 如果当前字符比前一个字符小，说明需要修改前一个字符
            if strNum[i - 1] > strNum[i]:
                # 将前一个字符减1，以保证递增性质
                # 使用字符串切片操作将修改后的前面部分与后面部分进行拼接
                strNum = strNum[:i - 1] + str(int(strNum[i - 1]) - 1) + '9' * (len(strNum) - i)       
        return int(strNum)