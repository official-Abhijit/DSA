class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for char in s:
            count[ord(char) - ord('a')] += 1

        for char in t:
            index = ord(char) - ord('a')
            count[index] -= 1

            if count[index] < 0:
                return False

        return True