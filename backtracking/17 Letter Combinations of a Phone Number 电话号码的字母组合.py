class Solution:
    def __init__(self):
        self.letterMap = [
            "",
            "",
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
        self.result = []

    def getConbinations(self, digits, index, s):
        if index == len(digits): #终止条件 比如 23，数组下标必须去到digits长度2才算真正结束
            self.result.append(s)
            return
        digit = int(digits[index]) #准备材料 比如 2 index是第几个字母
        letters = self.letterMap

        for letter in letters:
            self.getConbinations(digits, index + 1, s + letter)
            

    def letterConbnations(self, digits):
        if len(digits) == 0:
            return self.result
        self.getConbinations(digits, 0, "")
        return self.result


