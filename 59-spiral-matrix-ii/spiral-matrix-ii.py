class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        number = 1

        while top <= bottom and left <= right:
            # left to right
            for col in range(left, right + 1):
                matrix[top][col] = number
                number += 1
            top += 1

            # top to bottom
            for row in range(top, bottom + 1):
                matrix[row][right] = number
                number += 1
            right -= 1

            # right to left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = number
                    number += 1
                bottom -= 1

            # bottom to top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = number
                    number += 1
                left += 1

        return matrix