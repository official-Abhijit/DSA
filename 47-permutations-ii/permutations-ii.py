class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

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

                # Avoid starting the same choice twice at this level
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                current.append(nums[i])

                backtrack()

                current.pop()
                used[i] = False

        backtrack()
        return answer