

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
    
# 这是后来我自己的写法，有两个很奥妙的地方，这两点一定要分开看！
# 第一点是回溯方式：一个用了 path.append(...) + path.pop()（显式回溯） 一个用了字符串拼接 current + sub + '.'（隐式构造新值，不修改原始 current）
# 第二点是引用传递的问题：第一用方法path是str类型，是不可变类型，但是第二种方法里面用了list，是可变类型。这才是导致我们在res添加答案的时候，前者往里加了然后不用去掉，但是后者加了之后一定要pop的原因
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.backtracking(s, res, [], 0, 0)
        return res

    def backtracking(self, s, res, path, startIndex, sum):
        if sum == 3:
            if self.valid(s[startIndex:]):
                path.append(s[startIndex:])
                res.append(".".join(path[:]))
                path.pop()
            return 
        for i in range(startIndex, len(s)):
            if not self.valid(s[startIndex:i+1]):
                break
            path.append(s[startIndex:i+1])
            sum += 1
            self.backtracking(s, res, path, i+1, sum)
            sum -= 1
            path.pop()
            
    def valid(self, s):
        if not s:
            return False
        m = int(s)
        if len(s) > 1 and s[0] == '0':
            return False
        if m < 0 or m > 255:
            return False
        return True

