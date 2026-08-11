class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])

        sums = set()

        for r in range(rows):
            for c in range(cols):
                sums.add(grid[r][c])

                size = 1

                while (
                    r + 2 * size < rows
                    and c - size >= 0
                    and c + size < cols
                ):
                    total = 0

                    # top -> right
                    for k in range(size):
                        total += grid[r + k][c + k]

                    # right -> bottom
                    for k in range(size):
                        total += grid[r + size + k][c + size - k]

                    # bottom -> left
                    for k in range(size):
                        total += grid[r + 2 * size - k][c - k]

                    # left -> top
                    for k in range(size):
                        total += grid[r + size - k][c - size + k]

                    sums.add(total)
                    size += 1

        return sorted(sums, reverse=True)[:3]