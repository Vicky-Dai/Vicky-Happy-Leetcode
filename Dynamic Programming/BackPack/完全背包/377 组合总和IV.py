#和518零钱兑换是一样的，只不过求排列
#本题和爬楼梯是一样的，爬楼梯也要强调顺序是排列，这两题代码是一样的，爬楼梯的几步其实就是
#面试题，很喜欢这种逐步深入，比如先给一个普通的爬楼梯（一次1步或者两步）；一次多步的爬楼梯其实对应的就是这里的物品；然后问你这是排列还是组合，遍历顺序是否能改变？

class Solution:
    def conbinationSum4(self, nums: list[int], target:int) -> int:
        dp = [0] * (target + 1) #记得+1 下表和长度的关系
        dp[0] = 1 #既然递归公式是 dp[i] += dp[i - j]，那么dp[0] 一定为1，dp[0]是递归中一切数值的基础所在，如果dp[0]是0的话，其他数值都是0了。
        for i in range(1, target + 1): #遍历背包  注意range是左闭右开
            for j in nums:
                dp[i] += dp[i-j]
        return dp[target]