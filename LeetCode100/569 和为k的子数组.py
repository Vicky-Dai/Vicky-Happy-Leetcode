# 前缀和+哈希表
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        pre = 0
        mp = defaultdict(int)
        mp[0] = 1 # 为了处理从第一个元素开始就满足条件的情况
        
        for num in nums:
            pre += num
            if pre - k in mp:
                count += mp[pre - k] # 中间如果出现负数或0 就有可能出现多个相同的pre
            mp[pre] += 1
        
        return count
        