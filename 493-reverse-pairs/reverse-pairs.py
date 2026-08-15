class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        temp = [0] * len(nums)

        def merge_sort(left, right):
            if right - left <= 1:
                return 0

            mid = (left + right) // 2
            count = merge_sort(left, mid) + merge_sort(mid, right)

            j = mid

            for i in range(left, mid):
                while j < right and nums[i] > 2 * nums[j]:
                    j += 1

                count += j - mid

            i = left
            j = mid
            k = left

            while i < mid and j < right:
                if nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[j]
                    j += 1

                k += 1

            while i < mid:
                temp[k] = nums[i]
                i += 1
                k += 1

            while j < right:
                temp[k] = nums[j]
                j += 1
                k += 1

            for i in range(left, right):
                nums[i] = temp[i]

            return count

        return merge_sort(0, len(nums))