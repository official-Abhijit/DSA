class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = [0] * 26

        for char in s:
            count[ord(char) - ord('a')] += 1

        for i, char in enumerate(s):
            if count[ord(char) - ord('a')] == 1:
                return i

        return -1