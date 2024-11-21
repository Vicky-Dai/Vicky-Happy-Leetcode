#可以组成个多少个子序列
#dp[i][j] i-1为结尾的字符串s中有j-1为结尾的字符串t的个数

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        
        # Initialize dp array
        for i in range(len(s) + 1):
            dp[i][0] = 1  # Any string s with empty string t has one match
        
        for j in range(1, len(t) + 1):
            dp[0][j] = 0  # Empty string s with any non-empty string t has zero matches
        
        # Fill dp array and print the process
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]  #前者是用当前相等项目匹配（这时候要找之前跟当前项可以匹配的有多少个，比如bag：帮g找之前有几个ba）；后者是不用当前项匹配，可以理解为，没有加上当前项的匹配数（之前就有匹配上的，那么这时候t就不能变短，s要扔掉当前项）
                else:
                    dp[i][j] = dp[i - 1][j]
                
                # Print the current state of dp array
                print(f"dp[{i}][{j}] = {dp[i][j]}")
        
        # Print the final dp array
        print("Final dp array:")
        for row in dp:
            print(row)
        
        return dp[-1][-1]

# Example usage
s = "babgbag"
t = "bag"
solution = Solution()
print(f"Number of distinct subsequences: {solution.numDistinct(s, t)}")