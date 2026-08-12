class Solution:
    def smallestBalancedIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        right_sum = 0
        right_product = 1
        limit = total + 1
        answer = -1

        for i in range(len(nums) - 1, -1, -1):
            left_sum = total - right_sum - nums[i]

            if left_sum == right_product:
                answer = i

            right_sum += nums[i]
            right_product = min(limit, right_product * nums[i])

        return answer