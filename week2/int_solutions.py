from math import floor, sqrt

# Only whole numbers for solutions 
# Ordering matters, but if it's x = 5, y = 5, then print it only once

a = int(input())
b = int(input())
pair_count = 0

# All possible integers x and y, such that x + y = a and x * y = b

def find_factors(n):
    """
    Finds factors of a number. 
    Factors of 0 for clarity respresented as 0 * 0, despite infinite possibility of 0 * n.
    """
    factors = []
    sign = 1

    # Handle zero
    if n == 0:
        return [[0, 0]]

    # Handle negative numbers:
    if n < 0:
        sign = -1
        n = abs(n)

    for i in range(1, floor(sqrt(n)) + 1):
        if n % i == 0: # For all factors
            if (n // i == i): # Same number twice
                factors.append([i, i])

            elif (sign < 0): # Extra factors for negative numbers
                factors.append([i, (n // i)*sign])
                factors.append([(n // i)*sign, i])                

            else: # Standard case
                factors.append([i*sign, n // i])
                factors.append([n // i, i*sign])

    # print(factors)
    return factors

factors = find_factors(b)

for pair in factors:
    if (pair[0] + pair[1] == a):
        print(f"X = {pair[0]}, Y = {pair[1]}")
        pair_count += 1

if pair_count == 0:
    print('No solution')