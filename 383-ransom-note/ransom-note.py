class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0] * 26

        for char in magazine:
            count[ord(char) - ord('a')] += 1

        for char in ransomNote:
            index = ord(char) - ord('a')

            if count[index] == 0:
                return False

            count[index] -= 1

        return True