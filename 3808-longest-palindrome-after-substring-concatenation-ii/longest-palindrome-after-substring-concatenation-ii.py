class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def palindrome_bounds(x):
            n = len(x)
            start = [1] * n   # longest palindrome starting at i
            end = [1] * n     # longest palindrome ending at i

            for center in range(n):
                # odd length
                l = r = center

                while l >= 0 and r < n and x[l] == x[r]:
                    length = r - l + 1
                    start[l] = max(start[l], length)
                    end[r] = max(end[r], length)
                    l -= 1
                    r += 1

                # even length
                l = center
                r = center + 1

                while l >= 0 and r < n and x[l] == x[r]:
                    length = r - l + 1
                    start[l] = max(start[l], length)
                    end[r] = max(end[r], length)
                    l -= 1
                    r += 1

            return start, end

        s_start, _ = palindrome_bounds(s)
        _, t_end = palindrome_bounds(t)

        answer = max(max(s_start), max(t_end))

        m = len(t)

        # prev[j] = matching palindrome length using
        # previous position in s and position j in t
        prev = [0] * (m + 1)

        for i in range(len(s)):
            cur = [0] * (m + 1)

            for j in range(m - 1, -1, -1):
                if s[i] != t[j]:
                    continue

                cur[j] = 2 + prev[j + 1]

                middle = 0

                # Middle palindrome can lie in s
                if i + 1 < len(s):
                    middle = s_start[i + 1]

                # Or in t
                if j > 0:
                    middle = max(middle, t_end[j - 1])

                answer = max(answer, cur[j] + middle)

            prev = cur

        return answer