class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                if all(s[j] == s[j - i] for j in range(i, n)):
             #后面的每个字符，是否和它在前一个重复单元（长度为 i）中的对应字符一样。
                    return True
        return False

