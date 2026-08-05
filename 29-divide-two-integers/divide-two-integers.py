class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        # Only overflow case in 32-bit signed integer division
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            current_divisor = divisor
            multiple = 1

            # Double until the next doubled value is too large
            while current_divisor <= dividend - current_divisor:
                current_divisor <<= 1
                multiple <<= 1

            dividend -= current_divisor
            quotient += multiple

        return -quotient if negative else quotient