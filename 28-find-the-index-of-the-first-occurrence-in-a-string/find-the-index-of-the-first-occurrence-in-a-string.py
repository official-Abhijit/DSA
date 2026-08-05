class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)

        for start in range(len(haystack) - needle_length + 1):
            if haystack[start:start + needle_length] == needle:
                return start

        return -1