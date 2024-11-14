#背包有两个维度1和0
#递推公式 dp[i][j] = max(dp[i][j], dp[i-x][j-y]+1)  dp[i][j]的含义是背包放满m（i)个0， n个1，最多能放多少物品 xy分别是物品的0和1的个数
#dp[0][0] 非零下标也都初始化为0，才不会影响递推公式
#零一背包所有遍历都是先物品后背包，背包倒序

class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)] #注意0要加中括号！！！ 一维数组 二位数组，如果只是数字，那就只能成一维数组

        for str in strs:
            numZero = str.count('0')
            numOne = str.count('1')
            for i in range(m, numZero-1, -1):
                for j in range(n, numOne-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-numZero][j-numOne] + 1)
        return dp[m][n]
    


#打印版
class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for idx, str in enumerate(strs):
            numZero = str.count('0')
            numOne = str.count('1')
            print(f"Processing string {idx+1} ('{str}'): {numZero} zeros, {numOne} ones")
            for i in range(m, numZero - 1, -1):
                for j in range(n, numOne - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - numZero][j - numOne] + 1)
            
            # Print the dp table after processing each string
            print("DP table after processing this string:")
            for row in dp:
                print(row)
            print("\n" + "="*50 + "\n")

        return dp[m][n]

# Test the function
solution = Solution()
print("Final Result:", solution.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))