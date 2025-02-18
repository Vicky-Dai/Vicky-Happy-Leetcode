""" * """
#思路就是在当前覆盖范围内找下一步能覆盖最远的下标，然后更新当前覆盖范围，直到覆盖到终点
class Solution:
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        
        cur_distance = 0 #当前覆盖最远距离下标（用于判断要不要走到下一步）
        ans = 0
        next_distance = 0 #下一步覆盖最远距离下表

        for i in range(len(nums)):
            next_distance = max(i + nums[i], next_distance)
            if i == cur_distance: #下标走到了当前覆盖最远距离，因此要下一步
                ans += 1 #需要走下一步
                cur_distance = next_distance #更新当前覆盖最远距离下表：当前覆盖最远走到头，但是还是没覆盖终点，所以要取下一步里面最大的覆盖范围来继续判断
                if next_distance >= len(nums) - 1: #注意这里的位置，是在上一个if之内的，一定是先走再判断，而且是在走逻辑之内，因为如果不放在走逻辑内 1.放在前面，还没走就判断出去了 2. 放在后面但是外面，每次进来都要判断大不大于终点，要知道，i在遍历的时候，只是提前打量一下，而没有真的走，所以要放在走逻辑内
                    break

        return ans