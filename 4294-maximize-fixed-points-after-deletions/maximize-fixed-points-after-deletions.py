from bisect import bisect_right

class Solution:
    def maxFixedPoints(self, nums: List[int]) -> int:
        pairs = []

        for i, x in enumerate(nums):
            if x <= i:
                pairs.append((x, i - x))

        # x must be strictly increasing.
        # For equal x, sort deletion count descending
        # so LIS cannot select two equal values.
        pairs.sort(key=lambda p: (p[0], -p[1]))

        lis = []

        for _, deleted in pairs:
            pos = bisect_right(lis, deleted)

            if pos == len(lis):
                lis.append(deleted)
            else:
                lis[pos] = deleted

        return len(lis)