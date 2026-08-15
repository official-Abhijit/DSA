class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        offset = 10001
        size = 20002

        bit = [0] * (size + 1)
        answer = [0] * len(nums)

        def update(i):
            while i <= size:
                bit[i] += 1
                i += i & -i

        def query(i):
            total = 0

            while i > 0:
                total += bit[i]
                i -= i & -i

            return total

        for i in range(len(nums) - 1, -1, -1):
            index = nums[i] + offset

            # strictly smaller values
            answer[i] = query(index - 1)

            update(index)

        return answer