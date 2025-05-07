#时间复杂度 O(logn) 空间复杂度O(1)
#就用左闭右闭比较好控制

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 左闭右闭区间 [left, right]
        while left <= right:  # 当 left == right 时，区间 [left, right] 仍然有效
            mid = (left + right) // 2  # 计算中间索引
            if nums[mid] == target:  # 找到目标值
                return mid
            elif nums[mid] < target:  # 目标值在右半部分
                left = mid + 1  # 移动左边界到 mid + 1
            else:  # 目标值在左半部分
                right = mid - 1  # 移动右边界到 mid - 1
        return -1  # 未找到目标值，返回 -1
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