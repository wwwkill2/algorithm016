class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            pivot = matrix[mid // n][mid % n]
            if target == pivot:
                return True
            elif target < pivot:
                right = mid - 1
            else:
                left = mid + 1
        return False
