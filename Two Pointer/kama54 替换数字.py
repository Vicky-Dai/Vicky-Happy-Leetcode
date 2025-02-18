#O(n)

class Solution:
    def change(self, s):
        lst = list(s) # Python里面的string也是不可改的，所以也是需要额外空间的。空间复杂度：O(n)。
        for i in range(len(lst)):
            if lst[i].isdigit():
                lst[i] = "number"
        return ''.join(lst)
    
#join()是字符串对象的方法，它将可迭代对象（如列表或元组）中的每个元素用调用这个方法的字符串（在这里是空字符串''`）
#''.join(lst): 将列表中的元素依次拼接起来，中间没有任何分隔符。
