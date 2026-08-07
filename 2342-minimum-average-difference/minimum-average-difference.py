class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        min_diff = float("inf")
        answer = 0
        n = len(nums)

        for i in range(n):
            left_sum += nums[i]

            left_avg = left_sum // (i + 1)

            right_count = n - i - 1

            if right_count == 0:
                right_avg = 0
            else:
                right_sum = total_sum - left_sum
                right_avg = right_sum // right_count

            diff = abs(left_avg - right_avg)

            if diff < min_diff:
                min_diff = diff
                answer = i

        return answer