class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i, l = 0, len(nums)
        while i < l:
            if nums[i] == val: # 找到等于目标值的节点
                for j in range(i+1, l): # 移除该元素，并将后面元素向前平移
                    nums[j - 1] = nums[j]
                l -= 1
                i -= 1
            i += 1
        return l
    
#测试用例1
list1 = [3,2,2,3]
val1 = 3
print(Solution().removeElement(list1, val1)) #输出：2


#测试用例2        
list2 = [0,1,2,2,3,0,4,2]  #定义一个列表
val2 = 2
print(Solution().removeElement(list2, val2)) #输出：5