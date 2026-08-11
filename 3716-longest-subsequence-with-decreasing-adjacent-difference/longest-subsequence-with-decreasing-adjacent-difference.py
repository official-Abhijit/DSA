class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        MAX_VAL = 300
        MAX_DIFF = 299

        dp = [[0] * (MAX_DIFF + 1) for _ in range(MAX_VAL + 1)]
        seen = [False] * (MAX_VAL + 1)

        answer = 1

        for x in nums:
            add = [0] * (MAX_DIFF + 1)

            for prev in range(1, MAX_VAL + 1):
                if not seen[prev]:
                    continue

                diff = abs(x - prev)

                # Start a new pair
                length = 2

                # Or extend an existing subsequence
                if dp[prev][diff]:
                    length = max(length, dp[prev][diff] + 1)

                add[diff] = max(add[diff], length)
                answer = max(answer, length)

            # Convert exact differences into:
            # best length with last difference >= d
            best = 0

            for diff in range(MAX_DIFF, -1, -1):
                best = max(best, add[diff])
                dp[x][diff] = max(dp[x][diff], best)

            seen[x] = True

        return answer