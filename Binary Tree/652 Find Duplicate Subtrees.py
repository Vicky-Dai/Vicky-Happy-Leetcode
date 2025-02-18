#这道题我一开始的思路是没问题的，用哈希表记录遇到的子树，如果一个结果出现吵过一次，就发现重复子树
#但是这里要学到一个新的coding技巧：子树序列化

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(node: Optional[TreeNode]) -> str:
            if not node:
                return ""
            
            serial = "".join([str(node.val), "(", dfs(node.left), ")(", dfs(node.right), ")"])
            if (tree := seen.get(serial, None)): # python 3.8新特性，walrus operator :=，可以在表达式中赋值 也就是说，如果seen.get(serial, None)不为None，那么将其赋值给tree
                repeat.add(tree) #递归判断 添加
            else:
                seen[serial] = node
            
            return serial
        
        seen = dict()
        repeat = set() # 用set来存储重复的子树 set保证值被添加一次

        dfs(root)
        return list(repeat)

