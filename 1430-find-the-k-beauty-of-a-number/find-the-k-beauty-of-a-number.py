class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        count = 0

        for i in range(len(s) - k + 1):
            value = int(s[i:i + k])

            if value != 0 and num % value == 0:
                count += 1

        return count