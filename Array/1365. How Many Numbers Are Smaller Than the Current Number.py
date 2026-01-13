class Solution:
    # 方法一：使用字典
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = nums[:]
        hash_dict = dict()
        res.sort() # 从小到大排序之后，元素下标就是小于当前数字的数字
        for i, num in enumerate(res):
            if num  not in hash_dict.keys(): # 遇到了相同的数字，那么不需要更新该 number 的情况
                hash_dict[num] = i       
        for i, num in enumerate(nums):
            res[i] = hash_dict[num]
        return res

    # 方法二：使用数组
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # 同步进行排序和创建新数组的操作，这样可以减少一次冗余的数组复制操作，以减少一次O(n) 的复制时间开销
        sort_nums = sorted(nums)
        # 题意中 0 <= nums[i] <= 100，故range的参数设为101
        hash_lst = [0 for _ in range(101)]
        # 从后向前遍历，这样hash里存放的就是相同元素最左面的数值和下标了
        for i in range(len(sort_nums)-1,-1,-1):
            hash_lst[sort_nums[i]] = i
        for i in range(len(nums)):
            nums[i] = hash_lst[nums[i]]
        return nums