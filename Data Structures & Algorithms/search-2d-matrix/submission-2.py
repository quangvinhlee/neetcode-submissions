class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        left = 0
        right = row * col - 1

        while left <= right:
             
            mid = (left + right) // 2

            r = mid // col
            c = mid % col

            if matrix[r][c] < target:
                left += 1

            if matrix[r][c] > target:
                right -= 1
            if matrix[r][c] == target:
                return True
        
        return False



        