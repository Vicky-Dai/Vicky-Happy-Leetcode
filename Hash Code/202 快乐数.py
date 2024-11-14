class Solution:
    def isHappy(self, n:int) -> bool:
        record = set()

        while True: #创建一个无限循环  会无限循环下去
            n = self.get_sum(n) #对自身方法的调用
            if n == 1:
                return True

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
            