#暴力法 时间复杂度O(n^2)
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


#（版本一）快慢指针法 时间复杂度O(n)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 快慢指针
        fast = 0  # 快指针
        slow = 0  # 慢指针
        size = len(nums)
        while fast < size:  # 不加等于是因为，a = size 时，nums[a] 会越界
            # slow 用来收集不等于 val 的值，如果 fast 对应值不等于 val，则把它与 slow 替换
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1 #合并写法
        return slow #直接返回slow是因为，每次while先填空然后再改slow，即使是0位置上填空了之后，slow是1，所以直接返回slow就好，不需要+1