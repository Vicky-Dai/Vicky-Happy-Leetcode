# 注意sum(nums[j..i−1])=preSum[i]−preSum[j]  长度是i-j  # 其实是说(i-1)-(j-1)
#一维
class NumArray:
    # 前缀和数组
    def __init__(self, nums: List[int]):
        # 输入一个数组，构造前缀和
        # preSum[0] = 0，便于计算累加和
        self.preSum = [0] * (len(nums) + 1)
        # 计算 nums 的累加和
        for i in range(1, len(self.preSum)):
            self.preSum[i] = self.preSum[i - 1] + nums[i - 1]

    # 查询闭区间 [left, right] 的累加和
    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right + 1] - self.preSum[left]

#prefix[i] 表示 前 i 个元素的和（nums[0..i-1]）

# 二维...
同理 要多加一层，以及通过画图来更加清楚

# 后缀和(积)
def suffix_product(nums):
    """
    返回后缀积数组 suPro
    suPro[i] = nums[i] * nums[i+1] * ... * nums[n-1]
    """
    n = len(nums)
    suPro = [0] * (n + 1)   # 多开一个空间，suPro[n] = 1 表示空积

    suPro[n] = 1            # 空积初始化为1
    for i in range(n - 1, -1, -1):
        suPro[i] = suPro[i + 1] * nums[i]

    return suPro
