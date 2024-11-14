class Solution:
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        
        cur_distance = 0 #当前覆盖最远距离下标（用于判断要不要走到下一步）
        ans = 0
        next_distance = 0 #下一步覆盖最远距离下表

        for i in range(len(nums)):
            next_distance = max(i + nums[i], next_distance)
            if i == cur_distance:
                ans += 1 #需要走下一步
                cur_distance = next_distance #更新当前覆盖最远距离下表：当前覆盖最远走到头，但是还是没覆盖终点，所以要取下一步里面最大的覆盖范围来继续判断
                if next_distance >= len(nums) - 1:
                    break

        return ans