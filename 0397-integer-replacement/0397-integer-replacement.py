class Solution:
    def integerReplacement(self, n: int) -> int:
        # Initialize a counter for operations
        count = 0
        
        while n > 1:
            if n % 2 == 0:
                # If n is even, divide by 2
                n //= 2
            else:
                # If n is odd, decide to add or subtract 1
                if n == 3 or (n & 2) == 0:
                    n -= 1  # Subtract 1 if n is 3 or if the second last bit is 0
                else:
                    n += 1  # Otherwise, add 1
            count += 1
        
        return count