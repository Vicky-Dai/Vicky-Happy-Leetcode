class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list()
        for item in s:
            if res and res[-1] == item: #里面有元素且item和上一个相等
                res.pop()
            else:
                res.append(item)

        return "".join(res) #把栈里面剩下的元素拼接成字符串 只是为了把列表变成字符串而已