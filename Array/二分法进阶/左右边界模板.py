# left bound
def left_bound(nums: List[int], target: int) -> int:
    # 搜索左侧边界
    if len(nums) == 0:
        return -1
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            # 当找到 target 时，收缩右侧边界
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    return left

# right bound 
# 搜索右侧边界
def right_bound(nums: list[int], target: int) -> int:
    if len(nums) == 0:
        return -1
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            # 当找到 target 时，收缩左侧边界
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    return left - 1