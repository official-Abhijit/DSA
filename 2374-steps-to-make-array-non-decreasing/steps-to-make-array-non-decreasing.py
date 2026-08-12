class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []
        answer = 0

        for x in nums:
            steps = 0

            while stack and x >= stack[-1][0]:
                steps = max(steps, stack.pop()[1])

            if stack:
                steps += 1
            else:
                steps = 0

            answer = max(answer, steps)
            stack.append((x, steps))

        return answer