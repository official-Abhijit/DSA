class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = [0] * 26

        for ch in word:
            freq[ord(ch) - 97] += 1

        for i in range(26):
            if freq[i] == 0:
                continue

            freq[i] -= 1

            target = 0
            valid = True

            for count in freq:
                if count == 0:
                    continue

                if target == 0:
                    target = count
                elif count != target:
                    valid = False
                    break

            freq[i] += 1

            if valid:
                return True

        return False