

class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result = []
        self.backtracking(s, 0, 0, "", result)
        return result

    def backtracking(self, s, start_index, point_num, current, result):
        if point_num == 3: #终止条件是已经有了三个分隔点（ip地址有四块数字三个点）
            if self.is_valid(s, start_index, len(s)-1): #再判断一下第四段是合法的吗
                current += s[start_index:]
                result.append(current)
            return

        #单层逻辑
        for i in range(start_index, len(s)):
            if self.is_valid(s, start_index, i):
                sub = s[start_index : i+1]
                self.backtracking(s, i+1, point_num+1, current + sub + '.', result) #隐藏赋值
            else: 
                break


    def is_valid(self, s, start, end):
        if start > end:  # 前面backtracking的有一个传入是i+1, 当i走到len(s)-1的时候，下一次传入已经成为len(s) 会超出
            return False
        if s[start] == '0' and start != end: #不能前导是0，但是0本身可以
            return False
        num = 0
        for i in range(start, end + 1):
            if not s[i].isdigit(): #非法字符
                return False
            num = num * 10 + int(s[i]) #转换成整型
            if num > 225:
                return False
            
        return True