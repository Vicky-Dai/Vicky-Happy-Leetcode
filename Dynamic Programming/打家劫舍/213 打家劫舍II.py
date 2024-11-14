#注意范围只是遍历的范围，选不选某个元素是递推出来最优解决定的
#分情况讨论 1. 不考虑收尾，只考虑中间 2.考虑头和中间 3.考虑中间和尾   但是实际上23是包含了1的，因为只要覆盖的范围包含中间，就能包含中间的最大结果

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0: #如果没有房屋，返回0
            return 0
        if len(nums) == 1:
            return nums[0]
        
        #创建动态规划数组，用于存储最大金额
        result1 = self.robRange(nums, 0, len(nums) - 2) #情况二
        result2 = self.robRange(nums, 1, len(nums) - 1) #情况三
        return max(result1, result2)

    def robRange(self, nums: list[int], start:int, end: int):
        if end == start:
            return nums[start]
        
        dp = [0] * (end - start + 1)
        dp[0] = nums[start] #将dp的第一个元素设置为第一个房屋的金额
        dp[1] = max(nums[start], nums[start+1]) #将dp第二个元素设置为第一二个房屋中金额较大的

        #遍历剩余的房屋
        for i in range(2, end - start + 1):  #这里下标注意很容易出错  这里完全是新的数组的下标，所以找对应的nums所需要的数值的时候，需要通过start来表示
            #对于每个房屋，选择抢劫当前房屋和抢劫前一个房屋的最大金额
            dp[i] = max(dp[i-1], dp[i-2]+nums[start + i])

        return dp[-1]  #返回偷到的最大金额


#一维双指针
class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        result1 = self.robRange(nums, 0, len(nums) - 2)  # 情况二
        result2 = self.robRange(nums, 1, len(nums) - 1)  # 情况三
        return max(result1, result2)
    # 198.打家劫舍的逻辑
    def robRange(self, nums: list[int], start: int, end: int) -> int:
        if end == start:
            return nums[start]
        
        prev_max = nums[start]
        curr_max = max(nums[start], nums[start + 1])
        
        for i in range(start + 2, end + 1):
            temp = curr_max
            curr_max = max(prev_max + nums[i], curr_max)
            prev_max = temp
        
        return curr_max