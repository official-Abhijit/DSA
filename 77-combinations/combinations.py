class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        current = []

        def backtrack(start):
            if len(current) == k:
                result.append(current.copy())
                return

            for num in range(start, n + 1):
                current.append(num)
                backtrack(num + 1)
                current.pop()

        backtrack(1)
        return result