class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()

        n = len(nums)
        mid = (n - 1) // 2

        left = nums[:mid + 1][::-1]
        right = nums[mid + 1:][::-1]

        nums[::2] = left
        nums[1::2] = right