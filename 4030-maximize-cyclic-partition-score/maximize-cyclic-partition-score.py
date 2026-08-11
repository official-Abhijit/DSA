class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def solve(start):
            dp = [0] * (n + 1)
            answer = 0

            for _ in range(k):
                best_low = float("-inf")
                best_high = float("-inf")

                next_dp = [float("-inf")] * (n + 1)

                for j in range(n):
                    value = nums[(start + j) % n]

                    best_low = max(best_low, dp[j] - value)
                    best_high = max(best_high, dp[j] + value)

                    next_dp[j + 1] = max(
                        next_dp[j],
                        best_low + value,
                        best_high - value
                    )

                dp = next_dp
                answer = max(answer, dp[n])

            return answer

        min_index = min(range(n), key=lambda i: nums[i])

        return max(
            solve(min_index),
            solve((min_index + 1) % n)
        )