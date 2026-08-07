class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        remove_index = -1

        for i in range(len(number)):
            if number[i] == digit:
                remove_index = i

                if i + 1 < len(number) and number[i + 1] > digit:
                    break

        return number[:remove_index] + number[remove_index + 1:]