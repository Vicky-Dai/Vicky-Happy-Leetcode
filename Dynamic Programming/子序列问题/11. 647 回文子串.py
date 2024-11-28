#布尔类型的dp[i][j]：表示区间范围[i,j] （注意是左闭右闭）的子串是否是回文子串，如果是dp[i][j]为true，否则为false。
# 当s[i]与s[j]不相等，那没啥好说的了，dp[i][j]一定是false。

# 当s[i]与s[j]相等时，这就复杂一些了，有如下三种情况

# 情况一：下标i 与 j相同，同一个字符例如a，当然是回文子串
# 情况二：下标i 与 j相差为1，例如aa，也是回文子串
# 情况三：下标：i 与 j相差大于1的时候，例如cabac，此时s[i]与s[j]已经相同了，我们看i到j区间是不是回文子串就看aba是不是回文就可以了，那么aba的区间就是 i+1 与 j-1区间，这个区间是不是回文就看dp[i + 1][j - 1]是否为true。

class Solution:
    def CountSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        result = 0
        for i in range(len(s)-1, -1, -1): #注意遍历顺序
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1: #情况一 和 情况二
                        result += 1
                        dp[i][j] = True
                    elif dp[i+1][j-1]: #情况三  这里没理解？？
                        result += 1
                        dp[i][j] = True
        return result