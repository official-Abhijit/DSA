class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = {}

        # best1[j] = [length, ending_value]
        # best2[j] = second best with a different ending value
        best1 = [[0, None] for _ in range(k + 1)]
        best2 = [[0, None] for _ in range(k + 1)]

        answer = 0

        for x in nums:
            if x not in dp:
                dp[x] = [0] * (k + 1)

            # Descending so states from the current x
            # don't affect transitions with j - 1.
            for j in range(k, -1, -1):
                same = dp[x][j] + 1

                different = 1

                if j > 0:
                    if best1[j - 1][1] != x:
                        different = best1[j - 1][0] + 1
                    else:
                        different = best2[j - 1][0] + 1

                cur = max(same, different)
                dp[x][j] = cur

                # Update the two best endings for j
                if best1[j][1] == x:
                    if cur > best1[j][0]:
                        best1[j][0] = cur

                elif cur > best1[j][0]:
                    best2[j] = best1[j]
                    best1[j] = [cur, x]

                elif best2[j][1] == x:
                    if cur > best2[j][0]:
                        best2[j][0] = cur

                elif cur > best2[j][0]:
                    best2[j] = [cur, x]

                answer = max(answer, cur)

        return answer