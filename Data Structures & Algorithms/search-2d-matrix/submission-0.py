class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)*len(matrix[0]) -1
        while l <= r:
            mid = (l+r) // 2
            row = mid//len(matrix[0])
            actual_index = mid - (len(matrix[0]*row))
            if matrix[row][actual_index] < target:
                l = mid+1
            elif matrix[row][actual_index] > target:
                r = mid-1
            else:
                return True

        return False



        