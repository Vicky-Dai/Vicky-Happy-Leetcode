class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i>0 and nums[i] == nums[i-1]:
            continue #可以换成i += 1吗

        d = {}
        for j in range(i+1, len(nums)):
            if j > i+2 and nums[j] == nums[j-1] == nums[j-2]: #三元组元素b去重
                continue
            c = 0 - (nums[i] + nums[j])
            if c in d:
                result.append([nums[i], nums[j], c])
                d.pop(c)
            else:
                d[nums[j]] = j
    return result
#这里字典键存储的是第二个数字遍历过的数字，value是索引j，但是value并没有用到，用set()也可以

