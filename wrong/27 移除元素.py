class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                for j in range(i, len(nums)-1): #range(i, len(nums)-1) 代表的是[i, len(nums)-1)的范围
                    nums[j] = nums[j+1]
            else:    
                i+=1
          
        return len(nums) 


#错误点
# 1.首先python中如果数组有元素被彻底删除，len是会自动改变的，这是remove的底层代码所提供的方便，
#   然而自己在写removeElement的时候，运用的暴力覆盖法，并不会改变len(nums)的长度。 
# 2.长度没有改变问题不仅仅在于len(nums)返回有问题，更重要的是在于，如果后面有一个val,它会像
#   病毒一样把它前面和i之间全部改成这个val，但是由于你的数组长度即while边界没有改动，导致它会
#   一直卡在那里
            

#测试用例1
list1 = [3,2,2]
val1 = 3
print(Solution().removeElement(list1, val1)) #输出：2


