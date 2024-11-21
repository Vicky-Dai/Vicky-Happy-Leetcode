#连续子序列 

#dp[i][j] ：以下标i - 1为结尾的A，和以下标j - 1为结尾的B，最长重复子数组长度为dp[i][j]。 （特别注意： “以下标i - 1为结尾的A” 标明一定是 以A[i-1]为结尾的字符串 ）
#如果定义 dp[i][j]为 以下标i为结尾的A，和以下标j 为结尾的B，那么 第一行和第一列毕竟要进行初始化，如果nums1[i] 与 nums2[0] 相同的话，对应的 dp[i][0]就要初始为1， 因为此时最长重复子数组为1。 nums2[j] 与 nums1[0]相同的话，同理。

#brute force
def findLength(nums1, nums2):
    max_length = 0
    n1, n2 = len(nums1), len(nums2)
    
    for i in range(n1):  # 遍历 nums1 的起始点
        for j in range(n2):  # 遍历 nums2 的起始点
            k = 0  # 当前匹配长度
            while i + k < n1 and j + k < n2 and nums1[i + k] == nums2[j + k]: #相当于两个临时的指针
                k += 1
            max_length = max(max_length, k)  # 更新最长长度
            
    return max_length


#二维dp
class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        dp = [[0]*len(nums2) for _ in range(len(nums2))]
        result = 0
        for i in range(1, len(nums1)+1): #注意这个+1，因为定义里面是i-1 j-1,所以要走完全程要+1
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > result:
                    result =  dp[i][j]
        return result