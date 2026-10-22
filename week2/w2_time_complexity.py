# (1)
n = int(input())
if n % 2 == 0:
    print('even')
else:
    print('odd')

# (2)
n = int(input())
x = 1
for i in range(n): # n + 1
    for j in range(i): # n (outer loop) * ( triangular, loops up to k(k + 1) / 2 )
        x = 1 - x # same as above minus one truth check
print(x)

# (3)
n = int(input())
i = 1
while i < n:
    print('hello')
    i *= 3

# (4)
n = int(input())
s = 1
for i in range(n):
    for j in range(n):
        for k in range(n):
            s += 1
        s *= 2
    for l in range(n):
        s -= 1
    s //= 10
print(s)

# (5)
n = int(input())
w = 1
while n > 0:
    for x in range(n):
        w = (w * 31) % 2**16
    n //= 2