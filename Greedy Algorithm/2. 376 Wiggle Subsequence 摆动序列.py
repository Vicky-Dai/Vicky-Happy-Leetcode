#子序列：一个序列的子序列是由序列中的元素组成的一个序列，且这些元素在原序列中保持相对顺序不变。子序列可以由原序列中的任意多个元素组成，但不需要连续。
#删除操作本身复杂度就是On，所以没必要真的删除，就只遇到峰值就+1即可  但是这里注意，2个元素是2个摆动，1个元素是一个摆动
#除了上下普通摆动的特殊情况还要考虑 1.上下有平坡 2.首尾元素处理 3.单调有平坡

#我自己的写的版本
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        res = 1
        preDiff, curDiff = 0, 0
        for i in range(1, len(nums)):
            curDiff = nums[i] - nums[i-1]
            if (preDiff >= 0 and curDiff < 0) or (preDiff <= 0 and curDiff > 0):
                res += 1
                preDiff = curDiff
        return res
#我的思路：首先从头，和前面比较，如果是wiggle就+1，那么就少取一个头，所以res直接设置成1，每次wiggle了就加一个右侧的元素（和其他贪心固定一侧思路相同）
#其次，中间分情况，会出现，上下有平坡，还有单调有平坡这两种情况，总结就发现，首先curDiff不能是0，只有preDiff可以是0，if (preDiff >= 0 and curDiff < 0) or (preDiff <= 0 and curDiff > 0):所以0都在preDiff里；其次，preDiff的更新只有出现了wiggle的时候才更新
#总之，混乱的情况，总是应该先确定一个因素，比如preDiff为0还是curDiff为0， 左侧元素和右侧元素只能取一个， 固定一个之后看看能否推出一个规律


#原先版本
class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) <= 1:
            return len(nums) #如果数组长度为0或1，则返回数组长度
        curDiff = 0 #当前一堆元素的差值
        preDiff = 0 #前一对元素的差值
        result = 1 # 记录峰值的个数，初始为1（默认最右边的元素被视为峰值）(为了把两个数字的情况考虑进去，也为了能比较pre和cur的时候，最后一个点是没法比较的)
        for i in range(len(nums) - 1):
            curDiff = nums[i+1] - nums[i] #计算后坡
            if(preDiff<= 0 and curDiff > 0 ) or (preDiff >= 0 and curDiff <0 ): #！！！注意这里为了方便统计，只取左平右坡的情况，因为即使是在正常平坡（平坡两侧有坡），平坡也只能取一头  这里很重要！！
                result += 1
                preDiff = curDiff #这里是考虑特殊情况3的地方，唯一的改动就是把这一句code纳入到了if里面，就是说只有坡方向改变的时候，再去更新preDiff，这样就防止单调坡有平坡多算一个
        return result
            
