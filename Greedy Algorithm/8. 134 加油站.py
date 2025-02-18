#首先如果总油量减去总消耗大于等于零那么一定可以跑完一圈，说明 各个站点的加油站 剩油量rest[i]相加一定是大于等于零的。
#虽然代码没有直接体现回到起始点的过程，但我们可以通过简单的推理来验证。当车辆从 start 出发到达最后一个加油站后，我们可以把整个行程看作一个环形。此时剩余的油量，加上在前面已经走过的加油站中积累的油量（因为总油量足够），必然能够支持车辆从最后一个加油站回到 start 位置。
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        curSum = 0
        totalSum = 0
        start = 0 # 起始位置

        for i in range(len(gas)):
            curSum += gas[i] - cost[i] #用于计算走到现在还剩多少油，如果不符合要求后面会被重置
            totalSum += gas[i] - cost[i] #用于计算整条路上所有的油和消耗，判断整体是负还是正，是负的那肯定没有一个点能做到走完

            if curSum < 0:
                start = i + 1 # 起始位置更新为i+1 前面的路剩余油量为负都不行就都扔掉
                curSum = 0

        if totalSum < 0:
            return -1
        return start

        