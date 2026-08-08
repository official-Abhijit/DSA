class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [False] * (len(s2) + 1)
        dp[0] = True

        for j in range(1, len(s2) + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, len(s1) + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, len(s2) + 1):
                index = i + j - 1

                from_s1 = dp[j] and s1[i - 1] == s3[index]
                from_s2 = dp[j - 1] and s2[j - 1] == s3[index]

                dp[j] = from_s1 or from_s2

        return dp[-1]