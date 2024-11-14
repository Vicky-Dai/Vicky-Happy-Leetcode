#和分糖果一样，两个维度一定要一个维度一个维度去考虑，进行解耦  
class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda x:(-x[0], x[1])) #通过 -x[0]，较高的人会排在前面，因为负数的值越小代表原始值越大。  x[1] 它会在 x[0] 相等的情况下，按照从小到大的顺序进行排序。
        que = []

        #根据第二个维度进行插入
        for p in people:
            que.insert(p[1], p) #将元素 p 插入到列表 que 中的索引位置 p[1] 处。
        return que