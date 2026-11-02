perm = [int(x) for x in input().split()]

# Zachovam info o n na [0] i pro inverzni perm, jenom ji pak nevypisu
# Vzhledem k tomu ze input povazuje 1 za prvni pozici
inv_perm = [perm[0]] + [None] * perm[0]

for i in range(1, perm[0] + 1): # preskakuju n
    inv_perm[perm[i]] = i

print(" ".join(str(x) for x in inv_perm[1:]))