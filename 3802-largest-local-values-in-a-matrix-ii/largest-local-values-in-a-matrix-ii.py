class Solution:
    def countLocalMaximums(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        cells = [[] for _ in range(201)]
        for r in range(n):
            for c in range(m):
                if matrix[r][c] > 0:
                    cells[matrix[r][c]].append((r, c))

        bit = [[0] * (m + 1) for _ in range(n + 1)]

        def add(r, c):
            r += 1
            c += 1

            i = r
            while i <= n:
                j = c
                while j <= m:
                    bit[i][j] += 1
                    j += j & -j
                i += i & -i

        def prefix(r, c):
            if r < 0 or c < 0:
                return 0

            r += 1
            c += 1
            total = 0

            i = r
            while i > 0:
                j = c
                while j > 0:
                    total += bit[i][j]
                    j -= j & -j
                i -= i & -i

            return total

        def rectangle(r1, c1, r2, c2):
            return (
                prefix(r2, c2)
                - prefix(r1 - 1, c2)
                - prefix(r2, c1 - 1)
                + prefix(r1 - 1, c1 - 1)
            )

        answer = 0

        for x in range(200, 0, -1):
            # Fenwick currently contains only values > x
            for r, c in cells[x]:
                r1 = max(0, r - x)
                c1 = max(0, c - x)
                r2 = min(n - 1, r + x)
                c2 = min(m - 1, c + x)

                greater = rectangle(r1, c1, r2, c2)

                # Remove the four ignored corners
                for rr in (r - x, r + x):
                    for cc in (c - x, c + x):
                        if (
                            0 <= rr < n
                            and 0 <= cc < m
                            and matrix[rr][cc] > x
                        ):
                            greater -= 1

                if greater == 0:
                    answer += 1

            # Add cells of value x only after checking all of them.
            # Equal values do not invalidate each other.
            for r, c in cells[x]:
                add(r, c)

        return answer