class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() #记得排序一下
        
        for i in range(len(nums)):
            # 如果第一个元素已经大于0，不需要进一步检查
            if nums[i] > 0:
                return result
            
            # 跳过相同的元素以避免重复  这里用
            if i > 0 and nums[i] == nums[i - 1]:
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
                    
                    # 跳过相同的元素以避免重复
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                        
                    right -= 1
                    left += 1
                    
        return result

#如何保证不重复的？先sort，然后遍历数组，作为元组的第一个元素，然后left设定为i+1，right设定为len(nums)-1，然后开始遍历，如果三个数的和小于0，left右移，如果大于0，right左移，如果等于0，就是我们要找的，然后left右移，right左移，然后跳过重复的元素，继续遍历。