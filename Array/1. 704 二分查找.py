#时间复杂度 O(logn) 空间复杂度O(1)
#就用左闭右闭比较好控制

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left<=right: #左闭右闭 [2,2]也有意义 如果左闭右开[2,2) 就失去了意义
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid-1
            else: 
                right = mid+1
        return -1
if __name__ == "__main__":
    solution = Solution()

    # 测试用例1
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    result = solution.search(nums, target)
    print(f"在数组 {nums} 中查找 {target} 的结果是索引: {result}")

     # 测试用例2
    nums = [10, 20, 30, 40, 50]
    target = 25
    result = solution.search(nums, target)
    print(f"在数组 {nums} 中查找 {target} 的结果是索引: {result}")

    # 测试用例3
    nums = []
    target = 1
    result = solution.search(nums, target)
    print(f"在数组 {nums} 中查找 {target} 的结果是索引: {result}")