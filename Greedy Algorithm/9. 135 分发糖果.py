#不能左右一起比较
#从前往后比右大，从后往前比做大，要单边进行
#为什么第二轮要从前往后呢 如果我们单纯从前向后遍历数组 rating，当我们处理到第 i 个孩子时，我们只能根据 rating[i] 和 rating[i - 1] 的大小关系来决定给第 i 个孩子分配多少糖果。也就是说，我们只能利用前面已经处理过的孩子的信息，而无法利用后面孩子的信息。

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        
        # Forward pass: handle cases where right rating is higher than left
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Backward pass: handle cases where left rating is higher than right
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]: 
                candies[i] = max(candies[i], candies[i + 1] + 1) #这行代码起到了关键作用，max中 candies[i]保证了第一次遍历从左到右的结果能够保证，candies[i + 1] + 1保证了第二次遍历从右到左的结果能够保证
        
        return sum(candies)


#解惑：为什么两头的元素只比较一侧也能得出正确结果？
#起始元素：起始元素 ratings[0] 没有前一个元素与之比较，所以它初始化为 1 颗糖果（candies = [1] * n）。由于没有更前面的元素，也就不存在 “评分更高需要更多糖果” 的情况，初始的 1 颗糖果符合 “每个孩子至少 1 颗糖果” 的条件。
#后续元素：对于后续元素，我们比较 ratings[i] 和 ratings[i - 1]，如果 ratings[i] > ratings[i - 1]，则 candies[i] = candies[i - 1] + 1，保证了每个孩子与前一个孩子的关系满足条件。