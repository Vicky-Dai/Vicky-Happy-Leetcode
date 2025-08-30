1. res = [0]*len(nums) 里面必须有一个数字 否则不论多长创建的都是空数组
2. 值传递，引用传递 可变类型，不可变类型
Python 中一切变量都是对象的引用，
但是否“看起来能改动”这个对象，取决于它是可变类型（mutable）还是不可变类型（immutable）。
🔹不可变类型（immutable types）：
这些类型的值一旦创建就不能被改变，所有修改其实都是创建了新对象：
int float str tuple bool frozenset
🔹可变类型（mutable types）：
这些类型的值可以在原地修改，不创建新对象：list dict set bytearray 自定义的类对象
作为参数传递的时候，一定要注意，比如下面的path参数，如果是传递不可变类型，那么不管在dfs怎么改动，外面的path值都不会改变。
dfs(grid, visited, i, j, path) 

不可变类型举个例子：这里是一个错误的代码（709）w改了，但是s完全没改
class Solution:
    def toLowerCase(self, s: str) -> str:
        for w in s:
            if ord(w) < 97:
                w = chr(ord(w)+32)
        return s

3. minDist = [] * (n+1)  # This will create just a empty array