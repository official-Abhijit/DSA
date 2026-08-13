from functools import lru_cache

class Solution:
    def countArrangement(self, n: int) -> int:

        @lru_cache(None)
        def dfs(mask):
            position = mask.bit_count() + 1

            if position > n:
                return 1

            ways = 0

            for num in range(1, n + 1):
                bit = 1 << (num - 1)

                if mask & bit:
                    continue

                if num % position == 0 or position % num == 0:
                    ways += dfs(mask | bit)

            return ways

        return dfs(0)