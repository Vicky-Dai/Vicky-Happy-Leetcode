#思路：怎样才能让摄像头最小呢？从给的例子也可以分析出，不要放在叶子节点！因为摄像头覆盖上下三层，放在叶子节点就浪费一层，所以从下往上看
#虽然头结点也有这个问题，但是叶子节点的数目是指数级的
#所以我们要从下往上看，局部最优：让叶子节点的父节点安摄像头，所用摄像头最少，整体最优：全部摄像头数量所用最少！
#大体思路就是从低到上，先给叶子节点父节点放个摄像头，然后隔两个节点放一个摄像头，直至到二叉树头结点。
#那么这两者如何实现呢，第一个问题用后序遍历，第二个问题用数字来给节点标注状态来显示。
#0：该节点未覆盖 1：该节点有摄像头 2：该节点有覆盖

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        result = 0
        if self.traversal(root, result) == 0:
            result[0] += 1
        return result
    
    def traversal(self, cur:TreeNode, result: list[int]) -> int:
        if not cur:  #注意这里细节，到null的时候一定要赋给2状态，这样才能保证叶子节点不需要放置摄像头
            return 2
        
        left = self.traversal(cur.left, result) #左
        right = self.traversal(cur.right, result) #右

        #中 处理逻辑 因为中节点本来也是父节点的左右 所以不要疑惑为什么中节点没有单独的traversal
        if left == 2 and right == 2:
            return 0 #返回给父节点 父节点状态是0，也就是未覆盖
        
        if left == 0 or right == 0:
            result[0] += 1
            return 1  #要保证下面的孩子都是覆盖状态，所以要加个摄像头
        
        if left == 1 or right == 1:
            return 2
        

# 我自己的思考：这个题目的难点在于如何定义状态，以及如何处理状态，这个题目的状态是三个状态，0：未覆盖 1：有摄像头 2：有覆盖
# 在分类处理的时候，左右各三个状态，连线之后，左侧有9种情况，右侧有9种情况，如果左右之间用的是或处理，那么左右都消掉，且处理，也是左右都消掉
# 然后处理状况也是有顺序的，特别是有交叉的部分，比如left==0||right==0 和 left==1||right==1 ,他俩在连线之后你会发现两种有交叉，这之后就要注意顺序，窍门是优先处理必须解决的情况，比如当前节点无覆盖就必须装摄像头