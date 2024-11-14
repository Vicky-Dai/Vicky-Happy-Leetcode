class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0]*26 #创建一个长度为26的list  lists are mutable ordered and indexed collections of objects
        for i in s: #for loop is used for iterating over a sequence(list tuple dict se or a string)
            record[ord(i)-ord("a")] += 1 #ord()function returns the number representing the unicode code of a specified character
#引号用于表示这是一个字符串 而不是别的
        for i in t:
            record[ord(i)-ord("a")] -= 1 #第一个字符串加 第二个字符串减 如果有剩下的就说明不是ana
        
        for i in range(26):
            if record[i] != 0:
                 #record数组如果有的元素不为零0，说明字符串s和t 一定是谁多了字符或者谁少了字符。
                 return False
        return True  #注意这一行的缩进，顶格，因为前面的检查loop要跑完

#复杂度O(n)
#将n定义为两个字符串的总长度，循环检查为constant 26，视为O（1）