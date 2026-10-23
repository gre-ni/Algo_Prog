# Optimising for leaving out even numbers

# Making it only for odd numbers
# Which I am doing by converting indexes to odd numbers and vice versa
def to_index(c):
    return (c - 3) // 2

def from_index(i):
    return 2 * i + 3

n = int(input())
is_prime = [True] * (to_index(n) + 1)
for p in range(3, n + 1, 2):
    if is_prime[to_index(p)]: # We found a prime
        for k in range(p * p, n + 1, 2 * p): # p = 3, n = 100
            is_prime[to_index(k)] = False

print(2, end=' ')
for i in range(3, n + 1, 2):
    if is_prime[to_index(i)]:
        print(i, end=' ')
print()