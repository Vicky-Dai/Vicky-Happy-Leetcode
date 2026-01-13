class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # len >= 2; sum%k == 0;
        n = len(nums)
        preSum = [0]*(n+1)
        mapp = {0:0} #!!!!!
        for i in range(1, n+1):
            preSum[i] = nums[i-1] + preSum[i-1]
            if preSum[i]%k not in mapp:
                mapp[preSum[i]%k] = i
            else:
                j = mapp[preSum[i]%k]
                if i-j >= 2: #!!!!!!!!!!!!!!
                    return True
        return False