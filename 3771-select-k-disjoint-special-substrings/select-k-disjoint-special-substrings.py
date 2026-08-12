class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        if k == 0:
            return True

        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            x = ord(ch) - 97
            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        for c in range(26):
            if first[c] == n:
                continue

            start = first[c]
            end = last[c]
            i = start
            valid = True

            while i <= end:
                x = ord(s[i]) - 97

                if first[x] < start:
                    valid = False
                    break

                end = max(end, last[x])
                i += 1

            if valid and not (start == 0 and end == n - 1):
                intervals.append((end, start))

        intervals.sort()

        count = 0
        prev_end = -1

        for end, start in intervals:
            if start > prev_end:
                count += 1
                prev_end = end

                if count >= k:
                    return True

        return False