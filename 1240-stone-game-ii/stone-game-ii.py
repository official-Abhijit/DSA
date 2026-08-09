from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dfs(i, m):
            if i >= n:
                return 0

            if i + 2 * m >= n:
                return suffix[i]

            best = 0

            for x in range(1, 2 * m + 1):
                opponent = dfs(i + x, max(m, x))
                current = suffix[i] - opponent

                best = max(best, current)

            return best

        return dfs(0, 1)