class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return 0

        minimum = min(nums)
        maximum = max(nums)

        if minimum == maximum:
            return 0

        bucket_size = max(1, (maximum - minimum) // (n - 1))
        bucket_count = (maximum - minimum) // bucket_size + 1

        bucket_min = [float("inf")] * bucket_count
        bucket_max = [float("-inf")] * bucket_count

        for num in nums:
            index = (num - minimum) // bucket_size
            bucket_min[index] = min(bucket_min[index], num)
            bucket_max[index] = max(bucket_max[index], num)

        answer = 0
        previous_max = minimum

        for i in range(bucket_count):
            if bucket_min[i] == float("inf"):
                continue

            answer = max(answer, bucket_min[i] - previous_max)
            previous_max = bucket_max[i]

        return answer