class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left, right, n = 0, len(nums) - 1, len(nums) - 1   #尽量不要变量叠加：比如n=len(nums)-1, right = n  如果后面n产生了变化 其他一系列会跟着变，容易出问题
        _newnums = [float('inf')] * len(nums)
        while left <= right:
          if nums[left]*nums[left] <= nums[right]*nums[right]:
            _newnums[n] = nums[right]*nums[right]
            right -= 1
            
          else :
           _newnums[n] = nums[left]*nums[left]
           left += 1

          n -= 1

        return _newnums 

solution = Solution()    #实例化对象 注意下面测试用例也是要用实例化对象进行调用  
#没有使用实例属性，所以可以直接用类来调用方法，这是因为你并没有在方法中使用self去引用类实例本身。
# 也就是说，该方法实际上可以被看作是一个静态方法，因为它只依赖于传入的参数。所以直接Solution()也可以
#但是！！不推荐 尽量还是养成实例化的好习惯 不然以后容易出错
# 静态方法的调用方式如下：
# 类名.静态方法名(参数) 
# 例如：
# Solution.sortedSquares([1,2,3,4,5]) 
    
#测试用例1
nums = [-4, -3, 0, 2, 5, 6] #定义一个列表
result = Solution().sortedSquares(nums)
print(f"在数组平方的结果是: {result}")

#测试用例2
nums = [-7, -3, 2, 3, 11]
result = Solution().sortedSquares(nums)
print(f"在数组平方的结果是: {result}")   




