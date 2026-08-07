class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = []

        for char in s:
            if char != "-":
                chars.append(char.upper())

        result = []
        count = 0

        for i in range(len(chars) - 1, -1, -1):
            if count == k:
                result.append("-")
                count = 0

            result.append(chars[i])
            count += 1

        return "".join(reversed(result))