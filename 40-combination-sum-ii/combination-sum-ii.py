class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        answer = []

        def backtrack(start, remaining, current):
            if remaining == 0:
                answer.append(current.copy())
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break

                current.append(candidates[i])

                backtrack(
                    i + 1,
                    remaining - candidates[i],
                    current
                )

                current.pop()

        backtrack(0, target, [])
        return answer