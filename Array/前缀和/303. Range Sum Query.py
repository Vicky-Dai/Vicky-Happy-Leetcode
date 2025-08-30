class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum = [0] * (len(nums) +1)
        for i in range(1, len(nums)+1):
            self.preSum[i] = nums[i-1] + self.preSum[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right+1] - self.preSum[left]