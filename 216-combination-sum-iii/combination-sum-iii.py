class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        current = []

        def backtrack(start, remaining):
            if len(current) == k:
                if remaining == 0:
                    result.append(current.copy())
                return

            for num in range(start, 10):
                if num > remaining:
                    break

                current.append(num)
                backtrack(num + 1, remaining - num)
                current.pop()

        backtrack(1, n)
        return result