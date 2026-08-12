class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # Already sorted
        sorted_string = True
        mn = mx = s[0]

        for i in range(1, n):
            if s[i] < s[i - 1]:
                sorted_string = False

            mn = min(mn, s[i])
            mx = max(mx, s[i])

        if sorted_string:
            return 0

        # For length 2, the only substring that could fix
        # a descending pair is the whole string, which is forbidden.
        if n == 2:
            return -1

        # Sort s[1:] if the minimum is already at the front,
        # or sort s[:-1] if the maximum is already at the end.
        if s[0] == mn or s[-1] == mx:
            return 1

        # If a minimum or maximum exists somewhere in the middle,
        # two operations are enough.
        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2

        return 3