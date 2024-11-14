class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            # 如果第一个元素已经大于0，不需要进一步检查
            if nums[i] > 0:
                return result
            
            # 跳过相同的元素以避免重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue  #注意这里是continue!! 如果是i+=1 继续下面 会导致跳过一些元素 每次i比left right进度慢一轮
                
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
                    
                    # 跳过相同的元素以避免重复
                    # 仍然要right > left因为前面位置有改变，有可能超出范围也有可能找到重复的所以要加上left< right
                    # 注意以下是else缩进内 因为目标是结果没有重复 只有找到结果的时候 需要再次考虑重复和移动问题
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