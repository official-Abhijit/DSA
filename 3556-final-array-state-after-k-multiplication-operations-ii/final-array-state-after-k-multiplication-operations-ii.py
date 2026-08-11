import heapq

class Solution:
    def getFinalState(
        self,
        nums: List[int],
        k: int,
        multiplier: int
    ) -> List[int]:

        MOD = 10**9 + 7
        n = len(nums)

        if multiplier == 1:
            return [num % MOD for num in nums]

        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)

        current_max = max(nums)

        while k > 0:
            value, index = heap[0]

            if value * multiplier > current_max:
                break

            heapq.heappop(heap)

            value *= multiplier
            nums[index] = value

            current_max = max(current_max, value)
            heapq.heappush(heap, (value, index))

            k -= 1

        heap.sort()

        full_rounds = k // n
        extra = k % n

        answer = [0] * n

        for pos, (value, index) in enumerate(heap):
            times = full_rounds

            if pos < extra:
                times += 1

            answer[index] = (
                value % MOD
                * pow(multiplier, times, MOD)
            ) % MOD

        return answer