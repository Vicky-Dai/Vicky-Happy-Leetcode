# 枚举法
# 当我们遍历到下标 i 时，我们只需要让 i 满足 arr i>arr i+1即可
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        ans = -1

        for i in range(1, n - 1):
            if arr[i] > arr[i + 1]:
                ans = i
                break
        
        return ans
