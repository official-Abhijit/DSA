class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: List[int]
    ) -> List[int]:

        n = len(s)
        chars = list(s)

        size = 1
        while size < n:
            size <<= 1

        prefix = [0] * (2 * size)
        suffix = [0] * (2 * size)
        best = [0] * (2 * size)
        length = [0] * (2 * size)
        left_char = [''] * (2 * size)
        right_char = [''] * (2 * size)

        for i in range(n):
            p = size + i
            prefix[p] = suffix[p] = best[p] = length[p] = 1
            left_char[p] = right_char[p] = chars[i]

        def merge(node):
            left = node * 2
            right = left + 1

            length[node] = length[left] + length[right]

            if length[left] == 0:
                prefix[node] = prefix[right]
                suffix[node] = suffix[right]
                best[node] = best[right]
                left_char[node] = left_char[right]
                right_char[node] = right_char[right]
                return

            if length[right] == 0:
                prefix[node] = prefix[left]
                suffix[node] = suffix[left]
                best[node] = best[left]
                left_char[node] = left_char[left]
                right_char[node] = right_char[left]
                return

            left_char[node] = left_char[left]
            right_char[node] = right_char[right]

            prefix[node] = prefix[left]
            suffix[node] = suffix[right]
            best[node] = max(best[left], best[right])

            if right_char[left] == left_char[right]:
                joined = suffix[left] + prefix[right]
                best[node] = max(best[node], joined)

                if prefix[left] == length[left]:
                    prefix[node] += prefix[right]

                if suffix[right] == length[right]:
                    suffix[node] += suffix[left]

        for node in range(size - 1, 0, -1):
            merge(node)

        answer = []

        for index, ch in zip(queryIndices, queryCharacters):
            if chars[index] != ch:
                chars[index] = ch

                node = size + index
                left_char[node] = right_char[node] = ch

                node //= 2
                while node:
                    merge(node)
                    node //= 2

            answer.append(best[1])

        return answer