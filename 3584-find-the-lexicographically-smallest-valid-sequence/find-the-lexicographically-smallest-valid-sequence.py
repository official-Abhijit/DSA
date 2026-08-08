class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        # suffix[i] = how many characters from the end of word2
        # can be matched using word1[i:]
        suffix = [0] * (n + 1)

        j = m - 1
        matched = 0

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
                matched += 1

            suffix[i] = matched

        result = []
        j = 0
        mismatch_used = False

        for i in range(n):
            if j == m:
                break

            # Exact match: always take it as early as possible
            if word1[i] == word2[j]:
                result.append(i)
                j += 1

            # Try using our one mismatch here
            elif not mismatch_used:
                remaining = m - j - 1

                if suffix[i + 1] >= remaining:
                    result.append(i)
                    j += 1
                    mismatch_used = True

        return result if j == m else []