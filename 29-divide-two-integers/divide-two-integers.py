class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        return sign * quotient
