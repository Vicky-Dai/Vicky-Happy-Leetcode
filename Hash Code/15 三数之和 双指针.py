class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                return result  #先考虑特殊情况 如果第一个元素已经大于0，不需要进一步检查
            if i > 0 and nums[i] == nums[i-1]: #第一个i为0时不检验，到下一个后看看之前是不是检查过
                continue
            
            left = i + 1
            right = len(nums) - 1

            while right > left:
                sum_ = nums[i] + nums[left] + nums[right]
                
                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    #跳过相同的元素
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1

                    right -= 1
                    left += 1           

        return result
                        
def test_threeSum():
    solution = Solution()

    # Test case 1: standard case with multiple solutions
    nums1 = [-1, 0, 1, 2, -1, -4]
    expected1 = [[-1, -1, 2], [-1, 0, 1]]
    result1 = solution.threeSum(nums1)
    print (result1)
                        
            

