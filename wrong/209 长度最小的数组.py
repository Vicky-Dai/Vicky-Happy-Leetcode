class Solution:
    def minSubArrayLen(self, s: int, nums: list[int]) -> int:
        left, right, sum, l = 0, 0, nums[0], len(nums)
        res = [float('inf')] * len(nums)
        min_len = float('inf')  #定义一个超大未知数
        while left <= right and right < l: #循环的逻辑分析非常重要，需要几个，以及什么时候退出  #什么时候需要嵌套？
            #一般来说题目要求得结果，就是一个循环，因为需要靠它终止，其次把数组遍历一遍又是一个循环
            if sum >= s:
                min_len = min(min_len, right - left + 1)  #取小
                sum = sum - nums[left]
                left += 1
            else:  #问题好像出在这里了，right到最后的时候，仍然会进入这个else，导致索引超出 
                right += 1
                sum = sum + nums[right]
        return min_len
solution = Solution()
#测试用例1
nums = [2,3,1,2,4,3]  
s = 7
result = solution.minSubArrayLen(s,nums)
print(f"最小的长度为:{result}")

                
                