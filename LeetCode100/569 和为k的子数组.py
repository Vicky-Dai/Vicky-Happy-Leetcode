# 前缀和 + 哈希表
#我们定义 pre[i] 为 [0..i] 里所有数的和，则 pre[i] 可以由 pre[i−1] 递推而来，即：
#pre[i]=pre[i−1]+nums[i]
#那么「[j..i] 这个子数组和为 k 」这个条件我们可以转化为
#pre[i]−pre[j−1]==k
#简单移项可得符合条件的下标 j 需要满足
#pre[j−1]==pre[i]−k

#
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        pre = 0
        mp = defaultdict(int)
        mp[0] = 1
        
        for num in nums:
            pre += num
            if pre - k in mp:
                count += mp[pre - k]
            mp[pre] += 1
        
        return count
        