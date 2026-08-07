class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = {}

        for arr in nums:
            for num in arr:
                count[num] = count.get(num, 0) + 1

        result = []

        for num, freq in count.items():
            if freq == len(nums):
                result.append(num)

        result.sort()
        return result