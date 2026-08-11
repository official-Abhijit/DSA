class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        rows = len(grid)

        value_rows = [0] * 101

        for r in range(rows):
            for value in set(grid[r]):
                value_rows[value] |= 1 << r

        dp = [-1] * (1 << rows)
        dp[0] = 0

        for value in range(1, 101):
            if value_rows[value] == 0:
                continue

            # Go backwards so the same value is not used twice
            for mask in range((1 << rows) - 1, -1, -1):
                if dp[mask] == -1:
                    continue

                available = value_rows[value] & ~mask

                while available:
                    bit = available & -available
                    new_mask = mask | bit

                    dp[new_mask] = max(
                        dp[new_mask],
                        dp[mask] + value
                    )

                    available -= bit

        return max(dp)