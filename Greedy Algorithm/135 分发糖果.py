#不能左右一起比较
#从前往后比右大，从后往前比做大，要单边进行

class Solution:
    def candy(self, ratings:list[int]) -> int:
        candyVec = [1] * len(ratings)

        #从左往右
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candyVec[i] = candyVec[i-1] + 1

        #从右往左
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]: #当前需要改变的是i，这样写起来比较统一
                candyVec[i] = max(candyVec[i], candyVec[i+1] + 1)  #在从左往右和从右往左中取一个大的，从而能实现两个条件都满足

        result = sum(candyVec)
        return result
