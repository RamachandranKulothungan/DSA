class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        left = 0
        right = len(matrix)-1
        row = 0
        while left <= right:
            # print(left, right)
            m = (left+right)//2
            if matrix[m][0] == target:
                return True
            if matrix[m][0] < target:
                left = m + 1
                if m+1 == len(matrix) or matrix[m+1][0] > target:
                    row = m
                    break
                continue
            right = m - 1

        # print(f"row: {row}, {matrix[row]}")
        left = 0
        right = len(matrix[row]) - 1
        while left <= right:
            m = (left+right)//2
            # print(left, right, m)
            if matrix[row][m] == target:
                return True
            if matrix[row][m] < target:
                left = m + 1
                continue
            right = m - 1
        return False
