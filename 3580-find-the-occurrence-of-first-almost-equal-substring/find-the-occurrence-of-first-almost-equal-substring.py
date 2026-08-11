class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def z_function(text):
            n = len(text)
            z = [0] * n
            left = right = 0

            for i in range(1, n):
                if i <= right:
                    z[i] = min(right - i + 1, z[i - left])

                while i + z[i] < n and text[z[i]] == text[i + z[i]]:
                    z[i] += 1

                if i + z[i] - 1 > right:
                    left = i
                    right = i + z[i] - 1

            return z

        n = len(s)
        m = len(pattern)

        forward = pattern + "#" + s
        z1 = z_function(forward)

        reversed_pattern = pattern[::-1]
        reversed_s = s[::-1]

        backward = reversed_pattern + "#" + reversed_s
        z2 = z_function(backward)

        for start in range(n - m + 1):
            left_match = min(m, z1[m + 1 + start])

            if left_match == m:
                return start

            reverse_start = n - (start + m)
            right_match = min(m, z2[m + 1 + reverse_start])

            if left_match + right_match >= m - 1:
                return start

        return -1