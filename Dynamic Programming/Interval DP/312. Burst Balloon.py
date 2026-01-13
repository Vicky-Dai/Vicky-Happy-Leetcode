# Time O(n3) Space(O(n2))
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # n balloons   number on it: nums array
        # burst ith, get nums[i-1]*nums[i]*nums[i+1] coins
        # if outbounds, treat as 1
        # return maximum coins integer
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)] 
    #dp[i][j] 表示：在开区间 (i, j) 内，把所有气球都打爆所能获得的最大分数。

        # 区间长度从小到大 左右区间边界不能被打爆
        for length in range(2, n):   # 至少 3 才有空间
            for i in range(0, n - length):
                j = i + length
                for k in range(i+1, j):  # 最后打谁？ #
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j]
                    )
# dp[i][k] 坐班区间(i,k) 所有气球已经打包后的最大得分
        return dp[0][n-1]       