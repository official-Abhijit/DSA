class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        diffs = set()

        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                if d > 0:
                    diffs.add(d)

        if not diffs:
            return 0

        diffs = sorted(diffs)

        def count(d):
            # dp[i] = number of valid subsequences of current length
            # ending at nums[i]
            dp = [1] * n

            for length in range(2, k + 1):
                prefix = [0] * (n + 1)

                for i in range(n):
                    prefix[i + 1] = (prefix[i] + dp[i]) % MOD

                new_dp = [0] * n
                left = 0

                for i in range(n):
                    while left < i and nums[i] - nums[left] >= d:
                        left += 1

                    new_dp[i] = prefix[left]

                dp = new_dp

            return sum(dp) % MOD

        answer = 0
        previous = 0

        for d in diffs:
            ways = count(d)
            answer = (answer + (d - previous) * ways) % MOD
            previous = d

        return answer
        