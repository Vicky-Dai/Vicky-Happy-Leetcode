#将饼干分给尽可能多的小孩
#先排序，有两种思路
#1. 从小到大，因为小胃口比较容易满足，那么先遍历小胃口，让小饼干早出去
#2. 从大到小，因为大胃口比较难满足，那么先遍历胃口，让能适合的饼干早出去
#想象一下现场

#小饼干优先 这个写起来比较简单，就记这个
class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        index = 0
        for i in range(len(s)): #先遍历饼干
            if index < len(g) and g[index] <= s[i]: #保证贪心因子不超出范围，并且饼干能喂饱这个小孩
                index += 1
        return index #返回满足的孩子的个数