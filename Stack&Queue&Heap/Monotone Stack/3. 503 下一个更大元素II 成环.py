#很妙的成环处理，可以作为一个模板，以后都这么处理，通过%取模来处理
#再转一圈，因为只会被后面大的覆盖，所以不用担心覆盖到错误的值

class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [-1] * n
        stack = [0]
        for i in range(1, n*2):
            if nums[i%n] <= nums[stack[-1]]:
                stack.append(i%n)  #后面多的部分，如果是情况12直接压入展中，一直留在zhan里
            else:
                while len(stack)!=0 and nums[i%n] > nums[stack[-1]]: #多的部分如果是这个情况，会得到和前面一样的结果，所以也不怕覆盖
                    result[stack[-1]] = nums[i%n]
                    stack.pop()
                stack.append(i%n)
        return result 