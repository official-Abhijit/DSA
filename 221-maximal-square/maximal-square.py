class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [0] * (cols + 1)
        max_side = 0

        for r in range(1, rows + 1):
            prev = 0

            for c in range(1, cols + 1):
                temp = dp[c]

                if matrix[r - 1][c - 1] == "1":
                    dp[c] = 1 + min(
                        dp[c],      # top
                        dp[c - 1],  # left
                        prev        # top-left
                    )

                    max_side = max(max_side, dp[c])
                else:
                    dp[c] = 0

                prev = temp

        return max_side * max_side