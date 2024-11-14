#给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

#你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

#再强调一遍，当出现需要查询一个元素是否出现过的时候就要考虑哈希表
#这时候需要一个哈希表来存放遍历过的元素，然后去询问这个集合某个元素是否遍历过
#这道题因为还要返回数组下标，所以不能只用set(只存key),要用map存键值对

#这道题并不要求一个数字只能用一次，所以不用删除

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        records = {} #创建一个dict, key是元素，value是下标

        for index, value in enumerate(nums): #遍历数组 index为下标 value为元素
            complement = target - value
            if complement in records:
                return [records[complement], index] #找到匹配，返回两个下标
            records[value] = index #没找到匹配，把访问过的元素和下标加入到map

            return [] #没找到匹配
