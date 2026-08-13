class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = {}

        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        answer = 0

        for x in freq:
            if x + 1 in freq:
                answer = max(answer, freq[x] + freq[x + 1])

        return answer