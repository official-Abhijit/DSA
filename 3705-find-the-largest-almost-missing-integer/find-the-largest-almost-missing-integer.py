class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        windows = [0] * 51

        for start in range(len(nums) - k + 1):
            seen = [False] * 51

            for i in range(start, start + k):
                seen[nums[i]] = True

            for x in range(51):
                if seen[x]:
                    windows[x] += 1

        for x in range(50, -1, -1):
            if windows[x] == 1:
                return x

        return -1