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

        