#其实跳几步无所谓，关键在于可跳的覆盖范围！
#不一定非要明确一次究竟跳几步，每次取最大的跳跃步数，这个就是可以跳跃的覆盖范围。
#这个范围内，别管是怎么跳的，反正一定可以跳过来。
#那么这个问题就转化为跳跃覆盖范围究竟可不可以覆盖到终点！
#贪心算法局部最优解：每次取最大跳跃步数（取最大覆盖范围），整体最优解：最后得到整体最大覆盖范围，看是否能到终点。

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        if len(nums) == 1: return True
        i = 0
        # python不支持动态修改for循环中变量,使用while循环代替！！！
        while i <= cover: #i只能在覆盖范围内去取新值，不在覆盖范围怎么跳也跳不过去
            cover = max(i + nums[i], cover)
            if cover >= len(nums) - 1: return True
            i += 1
        return False