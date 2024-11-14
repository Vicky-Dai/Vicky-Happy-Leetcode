class Solution:
    def intersection(self, nums1:list[int], nums2: list[int]) -> list[int]:
        table = {}
        res = set()
        for num in nums1:
            table[num] = table.get(num, 0) + 1

        for i in nums2:
            if i in table:
                res.add(i)
                del table[i]
