class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        left = 0
        answer = 0

        for right, x in enumerate(nums):
            freq[x] = freq.get(x, 0) + 1

            while freq[x] > k:
                y = nums[left]
                freq[y] -= 1
                left += 1

            answer = max(answer, right - left + 1)

        return answer