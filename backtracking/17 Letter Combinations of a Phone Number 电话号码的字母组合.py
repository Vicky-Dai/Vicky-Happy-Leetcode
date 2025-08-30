# 目前这个用的是字符串记录path，增加用的+=，每次都会创建新的字符串，
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.digits_map = [
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]
        res = []
        s = ""
        self.backtracking(digits, res, "", 0)
        return res
    def backtracking(self, digits, res, path, index):
        if len(path) == len(digits):
            res.append("".join(path))
            return
        digit = int(digits[index])
        for i in range(len(self.digits_map[digit])):
            path += self.digits_map[digit][i]
            self.backtracking(digits, res, path, index+1)
            path = path[:-1]


