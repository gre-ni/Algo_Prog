from math import floor, sqrt

# Only whole numbers for solutions 
# Ordering matters, but if it's x = 5, y = 5, then print it only once

def find_factors(n):
    """
    Finds factors of a number. 
    Factors of 0 returns None, as there are infinitely many variants.
    Numbers with no factors.
    """
    factors = []
    sign = 1

    # Handle zero
    if n == 0:
        return None

    # Handle negative numbers:
    if n < 0:
        sign = -1
        n = abs(n)

    for i in range(1, floor(sqrt(n)) + 1):
        if n % i == 0: # For all factors
            if (n // i == i): # Same number twice
                factors.append([i*sign, i*sign])

            elif (sign < 0): # Extra factors for negative numbers
                factors.append([i, (n // i)*sign])
                factors.append([(n // i)*sign, i])                

            else: # Standard case
                factors.append([i*sign, n // i])
                factors.append([n // i, i*sign])

    return factors

def main():
    a = int(input())
    b = int(input())
    pair_count = 0
    
    # Handle zero and end early in that case
    if b == 0:
        print(f"X = {a}, Y = {b}")
        print(f"X = {b}, Y = {a}")
        return
    
    # Handle every other case
    factors = find_factors(b) 

    for pair in factors:
        if (pair[0] + pair[1] == a):
            print(f"X = {pair[0]}, Y = {pair[1]}")
            pair_count += 1
        
        # Handle negative a
        elif ((pair[0]*-1) + (pair[1]*-1) == a): 
            print(f"X = {pair[0]*-1}, Y = {pair[1]*-1}")
            pair_count += 1

    if pair_count == 0:
        print('No solution')
        
if __name__ == "__main__":
    main()