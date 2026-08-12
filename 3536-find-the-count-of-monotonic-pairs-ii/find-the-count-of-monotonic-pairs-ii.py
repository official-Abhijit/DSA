class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        dp = [1] * (nums[0] + 1)

        for i in range(1, len(nums)):
            prev = nums[i - 1]
            cur = nums[i]

            prefix = [0] * (len(dp) + 1)

            for j, ways in enumerate(dp):
                prefix[j + 1] = (prefix[j] + ways) % MOD

            new_dp = [0] * (cur + 1)

            for x in range(cur + 1):
                limit = min(x, x + prev - cur)

                if limit >= 0:
                    limit = min(limit, len(dp) - 1)
                    new_dp[x] = prefix[limit + 1]

            dp = new_dp

        return sum(dp) % MOD