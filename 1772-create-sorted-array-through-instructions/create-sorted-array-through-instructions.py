class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        size = max(instructions) + 2
        bit = [0] * size

        def update(i):
            while i < size:
                bit[i] += 1
                i += i & -i

        def query(i):
            total = 0

            while i > 0:
                total += bit[i]
                i -= i & -i

            return total

        answer = 0

        for i, x in enumerate(instructions):
            less = query(x - 1)

            less_or_equal = query(x)
            greater = i - less_or_equal

            answer = (answer + min(less, greater)) % MOD

            update(x)

        return answer