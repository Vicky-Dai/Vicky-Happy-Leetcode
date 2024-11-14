#考虑下表i，偷到的最大金额为dp[i] 
#dp[i] 从 dp[i-1] 和 dp[i-2] + nums[j] 推导而来，现在要理解的一点是dp[i-1]一定包含i-1那一家吗，不一定，只是考虑范围
#初始化 dp[0]=nums[0] 只有一家肯定得偷 dp[1]=max(nums[0], nums[1])
#从前面推导过来的，所以一定是从前到后遍历


#一维
class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0: #如果没有房屋，返回0
            return 0
        if len(nums) == 1:
            return nums[0]
        
        #创建动态规划数组，用于存储最大金额
        dp = [0] * len(nums)
        dp[0] = nums[0] #将dp的第一个元素设置为第一个房屋的金额
        dp[1] = max(nums[0], nums[1]) #将dp第二个元素设置为第一二个房屋中金额较大的

        #遍历剩余的房屋
        for i in range(2, len(nums)):
            #对于每个房屋，选择抢劫当前房屋和抢劫前一个房屋的最大金额
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        return dp[-1]  #返回偷到的最大金额