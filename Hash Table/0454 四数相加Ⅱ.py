class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        hashmap = {}
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in hashmap:
                    hashmap[n1+n2] += 1
                else:  #如果不存在，下标初始化为1
                    hashmap[n1+n2] = 1
                
        count = 0 #初始化一个计数器 （题目要求的结果）
        for n3 in nums3:
            for n4 in nums4:
                key = -n3 - n4
                if key in hashmap:
                    count += hashmap[key]
        return count




