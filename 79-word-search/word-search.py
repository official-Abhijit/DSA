class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def backtrack(row, col, index):
            if index == len(word):
                return True

            if (
                row < 0 or row >= rows or
                col < 0 or col >= cols or
                board[row][col] != word[index]
            ):
                return False

            temp = board[row][col]
            board[row][col] = "#"

            found = (
                backtrack(row + 1, col, index + 1)
                or backtrack(row - 1, col, index + 1)
                or backtrack(row, col + 1, index + 1)
                or backtrack(row, col - 1, index + 1)
            )

            board[row][col] = temp

            return found

        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True

        return False