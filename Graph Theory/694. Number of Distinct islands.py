class Solution:
    def numDistinctIslands(self, grid):
        shapes = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j, path, dir):
            # 超出边界或遇到水（0）或已访问过（2），直接返回
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != 1:
                return

            # 标记当前陆地为已访问
            grid[i][j] = 2
            path.append(dir)

            # 四个方向搜索
            dfs(i, j - 1, path, 'l')  # 左
            dfs(i + 1, j, path, 'd')  # 下
            dfs(i, j + 1, path, 'r')  # 右
            dfs(i - 1, j, path, 'u')  # 上

            # 回溯标记
            path.append('b')

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    path = []
                    dfs(i, j, path, 'o')  # 'o' 表示起点
                    shapes.add(''.join(path))

        return len(shapes)
