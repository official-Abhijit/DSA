from bisect import bisect_left

class Solution:
    def countRectangles(
        self,
        rectangles: List[List[int]],
        points: List[List[int]]
    ) -> List[int]:

        by_height = [[] for _ in range(101)]

        for length, height in rectangles:
            by_height[height].append(length)

        for height in range(1, 101):
            by_height[height].sort()

        result = []

        for x, y in points:
            count = 0

            for height in range(y, 101):
                lengths = by_height[height]

                index = bisect_left(lengths, x)
                count += len(lengths) - index

            result.append(count)

        return result