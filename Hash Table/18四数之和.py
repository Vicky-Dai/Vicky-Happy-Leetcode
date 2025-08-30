class Solution:
    def fourSum(self, nums: list[int], target:int) -> list[int]:
        result = []
        nums.sort()
        n = len(nums)
        for i in range(n): #如果 i 达到最后一个元素 n-1,这里的 j 从 i+1 开始，这意味着当 i 是最后一个元素（即 i = n-1）时，j 会从 n 开始。但问题是 range(i+1, n) 在这种情况下会变成 range(n, n)，这是一个空范围，因此 j 循环不会被执行。
            if nums[i] > target and nums[i] > 0 and target > 0: #剪枝 如果一上来就大
                #三个条件缺一不可
                break  #这道题break用return result也可以，但是return result显然管得更宽，所以来说，在大的项目可能出问题
            if i > 0 and nums[i] == nums[i]: #去重
                continue
            for j in range(i+1, n):
                if nums[j] > target and target > 0:
                    break
                if j > i+1 and nums[j] == nums[j-1]: #!!注意 > i+1
                    continue
                left, right = j+1, n-1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        result.append[nums[i], nums[j], nums[left], nums[right]]
                        while left < right and nums[left] == nums[left+1]: #。虽然外层 while left < right 确保了 left 不会超过 right，但跳过重复数字的逻辑需要检查 left < right 来避免越界。
                            left += 1 #这里如果设置left< right  left和right挨着会不会下一步重叠？ 所以right-1 这样对吗   不对 因为到外层while会排除这种情况  所以直接left < right 即可
 
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1        
                        left += 1
                        right -= 1                       
                
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return result
    


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        l = len(nums)

        for i in range(l):
            if nums[i] > target and nums[i]>0 and target >0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, l):
                if nums[i] + nums[j] > target and target >0:
                    break
                if j > i+1 and nums[j] == nums[j-1]: # 去重
                    continue

                left, right = j+1, l-1

                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if sum < target:
                        left += 1
                    elif sum > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        left += 1
                        right -= 1
                       

                        while left < right and nums[left] == nums[left + 1]: #这里如果设置left< right  left和right挨着会不会下一步重叠？ 所以right-1 这样对吗   不对 因为到外层while会排除这种情况  所以直接left < right 即可
                            left += 1
                        
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                       
                
            return result # 这个版本return缩进错了
        

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        l = len(nums)

        for i in range(l):
            if nums[i] > target and nums[i]>0 and target >0:
                return result
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, l):
                if nums[i] + nums[j] > target and target >0:
                    return result  #这个版本 这里绝对不可以写return result 而要写break因为这里外层还有个循环， 直接return会影响到外层，也就是我说的大项目会影响到的原因
                if j > i+1 and nums[j] == nums[j-1]: # 去重
                    continue

                left, right = j+1, l-1

                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if sum < target:
                        left += 1
                    elif sum > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                       
                        while left < right and nums[left] == nums[left + 1]: #这里如果设置left< right  left和right挨着会不会下一步重叠？ 所以right-1 这样对吗   不对 因为到外层while会排除这种情况  所以直接left < right 即可
                            left += 1
                        
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1     
                
        return result

        

