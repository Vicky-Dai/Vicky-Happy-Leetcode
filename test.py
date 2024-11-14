class Solution:
    def minSubArrayLen(self, s: int, nums: list[int]) -> int:
        l = len(nums)
        left = 0
        right = 0
        min_len = float('inf')
        cur_sum = 0 #当前的累加值
        
        while right < l:
            cur_sum += nums[right]
            
            while cur_sum >= s: # 当前累加值大于目标值
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            
            right += 1
        
        return min_len if min_len != float('inf') else 0
    
solution = Solution()    

#测试用例1
nums = [2,3,1,2,4,3]  
s = 7
result = solution.minSubArrayLen(s,nums)
print(f"最小的长度为:{result}")
    