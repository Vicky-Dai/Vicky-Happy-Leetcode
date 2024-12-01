#这道题恶化上一道唯一的区别就是有一个寻址的过程，因为单调盏操作的是nums2但是结果存放的是nums1

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]):
        result = [-1]* len(nums1)
        stack = [0]
        for i in range(1, len(nums2)):
            if nums2[i] <= nums2[stack[-1]]:
                stack.append(i)
            else:
                while len(stack)!=0 and nums2[i] > nums2[stack[-1]]:
                    if nums2[stack[-1]] in nums1:
                        position = nums1.index(nums2[stack[-1]])
                        result[position] = nums2[i]
                    stack.pop() 
                stack.append(nums2[i]) #在 Python 中，列表用 .append() 方法来模拟栈操作，而不是 .push()
        return result