class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True

        total = maxChoosableInteger * (maxChoosableInteger + 1) // 2

        if total < desiredTotal:
            return False

        memo = {}

        def dfs(mask, remaining):
            if mask in memo:
                return memo[mask]

            for num in range(maxChoosableInteger, 0, -1):
                bit = 1 << (num - 1)

                if mask & bit:
                    continue

                # Win immediately
                if num >= remaining:
                    memo[mask] = True
                    return True

                # If opponent cannot win after this move,
                # current player can force a win.
                if not dfs(mask | bit, remaining - num):
                    memo[mask] = True
                    return True

            memo[mask] = False
            return False

        return dfs(0, desiredTotal)