class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
            # 因为while每次循环需要进行条件判断，而range函数不需要，直接生成数字，因此时间复杂度更低。
