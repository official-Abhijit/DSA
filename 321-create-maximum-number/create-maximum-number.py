class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def max_subsequence(nums, length):
            drop = len(nums) - length
            stack = []

            for num in nums:
                while stack and drop > 0 and stack[-1] < num:
                    stack.pop()
                    drop -= 1

                stack.append(num)

            return stack[:length]

        def merge(a, b):
            result = []

            while a or b:
                if a > b:
                    result.append(a[0])
                    a = a[1:]
                else:
                    result.append(b[0])
                    b = b[1:]

            return result

        answer = []

        start = max(0, k - len(nums2))
        end = min(k, len(nums1))

        for take1 in range(start, end + 1):
            take2 = k - take1

            part1 = max_subsequence(nums1, take1)
            part2 = max_subsequence(nums2, take2)

            candidate = merge(part1, part2)

            if candidate > answer:
                answer = candidate

        return answer