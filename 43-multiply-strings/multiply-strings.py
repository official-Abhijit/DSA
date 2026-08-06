class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                digit1 = ord(num1[i]) - ord("0")
                digit2 = ord(num2[j]) - ord("0")

                product = digit1 * digit2

                ones_position = i + j + 1
                tens_position = i + j

                total = product + result[ones_position]

                result[ones_position] = total % 10
                result[tens_position] += total // 10

        answer = "".join(map(str, result))

        return answer.lstrip("0")