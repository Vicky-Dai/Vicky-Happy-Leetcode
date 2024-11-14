class Solution:
    def minsubArrayLen(self, nums: list[int], s: int) -> int:
        left, right, l = 0, 0, len(nums)
        sum = 0
        minlenth = float('inf')
        while right < l:
            sum = sum + nums[right]
            while sum >= s:
                tempLen = right - left + 1
                minlenth = min(minlenth, tempLen)
                sum = sum - nums[left]
                left += 1
            right += 1
        return minlenth

solution = Solution() #记得带括号才是实例化

#测试用例
nums = [2,3,1,2,4,3]  #等于号
s = 7
result = solution.minsubArrayLen(nums, s) 
print(f"最小的子数组长度是{result}") #f"语法

        