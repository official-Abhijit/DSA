class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor_all = 0
        has_nonzero = False

        for x in nums:
            xor_all ^= x

            if x != 0:
                has_nonzero = True

        if xor_all != 0:
            return len(nums)

        if has_nonzero:
            return len(nums) - 1

        return 0