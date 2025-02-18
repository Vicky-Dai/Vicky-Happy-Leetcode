#时间复杂度 O(logn) 空间复杂度O(logn)
""" 题目中说了会 无限循环，那么也就是说求和的过程中，sum会重复出现，这对解题很重要！

正如：关于哈希表，你该了解这些！中所说，当我们遇到了要快速判断一个元素是否出现集合里的时候，就要考虑哈希法了。 """

class Solution:
    def isHappy(self, n:int) -> bool:
        record = set()

        while True: #创建一个无限循环  会无限循环下去
            n = self.get_sum(n) #对自身方法的调用
            if n == 1:
                return True
             # 如果中间结果重复出现，说明陷入死循环了，该数不是快乐数
            if n in record:
                return False #哈希表快速判断一个元素是否在表里
            else:
                record.add(n)   #如果没出现就加进去

    def get_sum(self, n) -> int:
        new_num = 0 #定义一个新的变量
        while n:
            n, r = divmod(n,10) #python内置函数，divmod(x,y)返回商（x//y）和余数（x%y）通过余数获取每个位置上的值
            new_num += r**2 
        return new_num #返回新的数值 求新的和
            

#使用集合方法二
class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()
        while n not in record:
            record.add(n)
            new_num = 0
            n_str = str(n) #将整数 n 转换为字符串 n_str，这样可以方便地逐位访问每个数字。
            for i in n_str:
                new_num += int(i)**2
            if new_num == 1: return True
            else: n = new_num
        return False
