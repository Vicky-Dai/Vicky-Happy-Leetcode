class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split()
        return " ".join(res[::-1])
# 这种解法使用了额外的空间， 也可以用双指针

# 如果