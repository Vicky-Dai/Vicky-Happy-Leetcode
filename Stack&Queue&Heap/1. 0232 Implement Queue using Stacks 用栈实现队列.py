class MyQueue:
    
    def __init__ (self):
        """
        入栈和出栈 in主要负责push, out主要负责pop
        """
        self.stack_in = []
        self.stack_out = []

    def push(self) -> int:
         """
         有新元素进来
         """
         self.stack_in.append(x)
    
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():  #注意这里的分情况
            return None
        
        if self.stack_out:
            return self.stack_out.pop() #出栈按顺序弹出就是队列的顺序
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
        #如果出栈还什么都没有，就按顺序吧所有的入栈元素一次压入出栈

    def peek(self) -> int:
        """
        Get the front element
        """
        ans = self.pop() #直接用self就指向的是当前类的实例对象所对应的方法，这里的pop是前面构造的pop
        self.stack_out.append(ans)
        return ans #复用pop 一种方便的代码管理方式 不要直接复制粘贴 可能埋雷
    
    def empt(self) -> bool:
        """
        只要in或者out有元素，说明队列不为空
        """
        return not(self.stack_in or self.stack_out)
    #not 是逻辑非运算符，用来取反。
#如果 self.stack_in 或 self.stack_out 中有元素，or 运算会返回一个非空的列表，而 not 会将其结果取反，返回 False。

  