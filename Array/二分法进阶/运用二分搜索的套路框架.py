# 函数 f 是关于自变量 x 的单调函数
def f(x: int) -> int:
    # ...
    return

# 主函数，在 f(x) == target 的约束下求 x 的最值
def solution(nums: List[int], target: int) -> int:
    if len(nums) == 0:
        return -1
    # 问自己：自变量 x 的最小值是多少？
    left = ...
    # 问自己：自变量 x 的最大值是多少？
    right = ... + 1

    while left < right:
        mid = left + (right - left) // 2
        if f(mid) == target:
            # 问自己：题目是求左边界还是右边界？
             ...
        elif f(mid) < target:
            # 问自己：怎么让 f(x) 大一点？
             ...
        elif f(mid) > target:
            # 问自己：怎么让 f(x) 小一点？
             ...
    return left