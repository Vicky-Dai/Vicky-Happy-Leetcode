class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c] # 都要处理所以放在if外
            node.word = word
        res = []

        def dfs(i, j, node):
            ch = board[i][j]
            if ch not in node.children:
                return 
            
            nxt = node.children[ch]
            if nxt.word: #收集结果
                res.append(nxt.word)
                nxt.word = None # 去重
            board[i][j] = '#' # 标记访问

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = i + dr, j + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)
            board[i][j] = ch # 回溯

            # 🌟 优化点：如果字典树节点已经没有孩子了，直接剪枝, 意味着不可能再找到别的单词了
            if not nxt.children:
                node.children.pop(ch)

        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)
        
        return res



