#多少种方式能把背包装满
#本道题有一个数学转换过程
#[1,1,1,1,1]  分成left right两个集合  left + right = sum   left - right = target   right = sum - right  整理一下 left = (target + sum) /2
#这里left就是要装的背包量 也就是最终要实现的j
#dp[j] 含义 ，装满j 有几种方法
#搞清楚dp[j]含义，如果目标是5，现在有1，那就需要dp[4]凑成dp[5]，仍然是dp[4]种方法；
#dp[5] = dp[4] + dp[3] + dp[2] + dp[1] + dp[0] => dp[j] += dp[j-nums[i]]
#初始化的话就代入一下，看看dp[0]究竟有几种方法  非0下标初始成0就行 为什么？？？

class Solution:
    def findTargetSumWays(self, nums:list[int], target: int) -> int:
        total_sum = sum(nums) #计算nums的总和
        if abs(target) > total_sum:
            return 0 #此时没有方案
        if (target + total_sum) % 2 == 1:
            return 0 # 此时没有方案
        target_sum = (target + total_sum) // 2 #目标和
        dp = [0] * (target_sum + 1) #创建动态规划数组，初始化为0
        dp[0] = 1 # 当目标和为0时，只有一种方案  为什么？？？
        for num in nums:
            for j in range(target_sum, num - 1, -1):
                dp[j] += dp[j - num]  # 状态转移方程，累加不同选择方式的数量
        return dp[target_sum]  # 返回达到目标和的方案数