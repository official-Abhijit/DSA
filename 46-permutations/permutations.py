class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        current = []
        used = [False] * len(nums)

        def backtrack():
            if len(current) == len(nums):
                answer.append(current.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                current.append(nums[i])

                backtrack()

                current.pop()
                used[i] = False

        backtrack()
        return answer