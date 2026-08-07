class Solution:
    def largestGoodInteger(self, num: str) -> str:
        answer = ""

        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                current = num[i:i + 3]

                if current > answer:
                    answer = current

        return answer