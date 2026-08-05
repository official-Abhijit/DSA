class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_first() -> int:
            left = 0
            right = len(nums) - 1
            answer = -1

            while left <= right:
                middle = (left + right) // 2

                if nums[middle] >= target:
                    right = middle - 1
                else:
                    left = middle + 1

                if nums[middle] == target:
                    answer = middle

            return answer

        def find_last() -> int:
            left = 0
            right = len(nums) - 1
            answer = -1

            while left <= right:
                middle = (left + right) // 2

                if nums[middle] <= target:
                    left = middle + 1
                else:
                    right = middle - 1

                if nums[middle] == target:
                    answer = middle

            return answer

        return [find_first(), find_last()]