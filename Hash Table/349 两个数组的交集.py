#时间复杂度 单词总字数是T  O（T）

class Solution:
    def intersection(self, nums1:list[int], nums2: list[int]) -> list[int]:
        table = {} #创建字典
        res = set() #创建集合
        for num in nums1:
            table[num] = table.get(num, 0) + 1

        for i in nums2:
            if i in table:
                res.add(i)
                del table[i] #删除对应的键i以及对应的值，省去一些没有必要的循环
        return list(res)
    

#这个找倍数的方法很奇怪每次都会想到，但是已经帮忙测过了，有问题，以后不要再想他了
#首先就是这个除法会是浮点数，以及如果在两个单词中某个单词各出现两次，另一个单词出现三次，仍然总体数量不是数组长度的倍数，这个导致不能保证倍数才是我们要的东西
# class Solution:
#     def commonChars(self, words: List[str]) -> List[str]:
#         array = [0] * 26
#         res = []
#         for i in range(len(words)):
#             for word in words[i]:
#                 array[ord(word)-ord('a')] += 1
#         for i in range(26):
#             if array[i] > 0 and array[i] % len(words) == 0:
#                 for j in range(int(array[i]/len(words))):
#                     res.append(chr(ord('a') + j))
#         return res