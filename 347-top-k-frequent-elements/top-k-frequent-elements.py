class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for x, count in freq.items():
            buckets[count].append(x)

        answer = []

        for count in range(len(nums), 0, -1):
            for x in buckets[count]:
                answer.append(x)

                if len(answer) == k:
                    return answer