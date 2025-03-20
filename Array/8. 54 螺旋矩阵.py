class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
    
        ans = []
        line_begin, line_end = 0, len(matrix[0]) - 1  # 行的开头与结尾
        list_begin, list_end = 0, len(matrix) - 1    # 列的开头与结尾
        
        while True:
            # 从左往右
            for i in range(line_begin, line_end + 1):
                ans.append(matrix[list_begin][i])
            list_begin += 1
            if list_begin > list_end:
                break
            
            # 从上往下
            for i in range(list_begin, list_end + 1):
                ans.append(matrix[i][line_end])
            line_end -= 1
            if line_end < line_begin:
                break
            
            # 从右往左
            for i in range(line_end, line_begin - 1, -1):
                ans.append(matrix[list_end][i])
            list_end -= 1
            if list_end < list_begin:
                break
            
            # 从下往上
            for i in range(list_end, list_begin - 1, -1):
                ans.append(matrix[i][line_begin])
            line_begin += 1
            if line_begin > line_end:
                break
        
        return ans