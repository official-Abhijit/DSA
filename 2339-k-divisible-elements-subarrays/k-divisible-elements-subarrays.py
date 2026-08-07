class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        seen = set()

        for i in range(len(nums)):
            divisible = 0
            current = []

            for j in range(i, len(nums)):
                current.append(nums[j])

                if nums[j] % p == 0:
                    divisible += 1

                if divisible > k:
                    break

                seen.add(tuple(current))

        return len(seen)