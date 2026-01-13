# dfs
def dfs(node):
    if not node:
        return None
    # if we do something with the node here, it will be in the preorder position
    dfs(node.left)
    # if we do something with the node here, it will be in the inorder position
    dfs(node.right)
    # if we do something with the node here, it will be in the postorder position
    ...
    return None
# 递归四部曲
1. 确定递归函数的参数和返回值
2. 确定终止条件
3. 确定单层递归的逻辑
4. 处理中间和最后一次返回值


# bfs
def bfs(node):
    if not node:
        return None
    queue = collections.deque([node])
    while queue:
        cur = queue.popleft()
        ...
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return ...