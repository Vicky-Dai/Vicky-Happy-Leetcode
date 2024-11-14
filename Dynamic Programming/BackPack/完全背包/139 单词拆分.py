#不要怕切割拆分这种字眼，其实就是类似组合，本题结合回溯131分割回文穿来看
#从动态规划的角度，物品能不能装满背包，单词能不能组成目标词组
#如果能组成长度为i数组，那么dp[i]就为true
#dp[i] = if([j,i] && dp[i] == true
#初始化 dp[0] = true 本题0无意义，但是如果是false就把后面全覆盖了，非零下标必须是false，否则全都true（其他下表还不知道是否能组成 ？？？
#本题对顺序有要求，所以是排列，先背包再物品


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)  # dp[i] 表示字符串的前 i 个字符是否可以被拆分成单词
        dp[0] = True  # 初始状态，空字符串可以被拆分成单词

        for i in range(1, n + 1): # 遍历背包
            for j in range(i): # 遍历单词
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True  # 如果 s[0:j] 可以被拆分成单词，并且 s[j:i] 在单词集合中存在，则 s[0:i] 可以被拆分成单词
                    break

        return dp[n]