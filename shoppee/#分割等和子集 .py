#能不能装满背包，能 return True  不能 False
#给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
#如何转化成背包问题? 很巧妙
#首先分割成两个子集，例如[1, 5, 11, 5] 总和22，一半是11，找到和为11的，相当于说用这些物品，能不能装满一个11的包，如果可以就是行
#那么这里，重量和价值是等价的，11容量的背包价值为11，也就是dp[target] == target
#dp[j] 表示： 容量（所能装的重量）为j的背包，所背的物品价值最大可以为dp[j]。

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        _sum = 0

        # dp[i]中的i表示背包内总和
        # 题目中说：每个数组中的元素不会超过 100，数组的大小不会超过 200
        # 总和不会大于20000，背包最大只需要其中一半，所以10001大小就可以了

        dp = [0] * 10001
        for num in nums:
            _sum += num
        
         # 也可以使用内置函数一步求和
        # _sum = sum(nums)
        if _sum % 2 == 1:  #必须是偶数
            return False
        target = _sum // 2

        #开始0-1背包
        for num in nums:
            for j in range(target, num-1, -1):  # 每一个元素一定是不可重复放入，所以从大到小遍历  #逆向：从target开始，是说最终最大的目标是target     stone - 1, 是因为当前j如果小于stone, 根本放不进去当前物品，只能维持原先的dp[j],相当于跳过    逆序左闭右开，实际上只能能走到stone
                dp[j] = max(dp[j], dp[j - num] + num)

        #集合中的元素刚好可以凑成总和target
        if dp[target] == target:
            return True
        return False