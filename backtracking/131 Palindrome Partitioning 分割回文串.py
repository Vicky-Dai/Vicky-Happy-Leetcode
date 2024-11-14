'''
        递归用于纵向遍历
        for循环用于横向遍历
        当切割线迭代至字符串末尾，说明找到一种方法
        类似组合问题，为了不重复切割同一位置，需要start_index来做标记下一轮递归的起始位置(切割线)
        '''
class Solution:
    def patition(self, s: str) -> list[list[str]]:
        result = []
        self.backtracking(s, 0, [], result)
        return result
    
    def backtracking(self, s, start_index, path, result):
        if start_index == len(s): #终止条件：切割结束，切割线在start_index右侧
            result.append(path[:])
            return #判断回文放在单层处理逻辑了
        
        #单层递归
        for i in range(start_index, len(s)): #i是一把刀    vvvvvvvvvvvvvv                                                                                                                                                                                                                                                                                                                                    
            if self.is_palindrome(s, start_index, i):  #注意这里是i, 写参数的时候，先定义形参，再根据形参写实参
                path.append(s[start_index:i+1]) #左闭右闭
                self.backtracking(s, i+1, path, result) # 递归纵向遍历：从下一处进行切割，判断其余是否仍为回文串
                path.pop() #回溯

    def is_palindrome(self, s, start: int, end: int) -> bool:
        i: int = start        
        j: int = end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True 