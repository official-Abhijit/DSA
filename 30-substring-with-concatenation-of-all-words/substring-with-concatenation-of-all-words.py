from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []

        required = Counter(words)
        result = []

        for offset in range(word_len):
            left = offset
            right = offset
            current = Counter()
            used = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in required:
                    current[word] += 1
                    used += 1

                    while current[word] > required[word]:
                        left_word = s[left:left + word_len]
                        current[left_word] -= 1
                        left += word_len
                        used -= 1

                    if used == word_count:
                        result.append(left)

                        left_word = s[left:left + word_len]
                        current[left_word] -= 1
                        left += word_len
                        used -= 1

                else:
                    current.clear()
                    used = 0
                    left = right

        return result